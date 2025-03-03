from flask import Flask, request, jsonify
import requests
import mysql.connector
import os
import time
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, supports_credentials=True)

# MySQL Configuration
DB_CONFIG = {
    "host": os.environ.get("MYSQL_HOST", "localhost"),
    "user": os.environ.get("MYSQL_USER", "root"),
    "password": os.environ.get("MYSQL_PASSWORD", "password"),
    "database": "crypto_db"
}

# API to fetch crypto prices
COIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,xrp&vs_currencies=usd"

def get_crypto_prices():
    response = requests.get(COIN_API_URL)
    if response.status_code == 200:
        return response.json()
    return {}

def initialize_database():
    print("Initializing database...")
    max_retries = 5
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            conn = mysql.connector.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"]
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS crypto_db")
            cursor.close()
            conn.close()
            
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS crypto_prices (
                id INT AUTO_INCREMENT PRIMARY KEY,
                coin_name VARCHAR(10) NOT NULL,
                price DECIMAL(18,8) NOT NULL,
                timestamp DATETIME NOT NULL
            )
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            print("Database and table are initialized.")
            return
        except mysql.connector.Error as db_err:
            print(f"Database initialization error (attempt {attempt+1}/{max_retries}): {db_err}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Database connection failed. Exiting.")
                exit(1)

def save_to_db(coin_name, price):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO crypto_prices (coin_name, price, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(query, (coin_name, price, datetime.utcnow()))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Successfully saved {coin_name}: ${price}")
        return True
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return False

@app.route('/fetch_price', methods=['GET'])
def fetch_price():
    prices = get_crypto_prices()
    if prices:
        results = []
        for coin, data in prices.items():
            success = save_to_db(coin, data['usd'])
            results.append({"coin": coin, "price": data['usd'], "saved": success})
            if not success:
                print(f"Failed to save {coin}: ${data['usd']}")
        return jsonify(results)
    print("Error: Failed to fetch prices from API")
    return jsonify({"error": "Failed to fetch prices"}), 500

if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=5001, debug=True)