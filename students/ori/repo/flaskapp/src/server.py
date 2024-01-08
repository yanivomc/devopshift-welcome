from flask import Flask, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MySQL Connection Configuration
config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'raise_on_warnings': True
}

# Function to save user to the database
def save_user_to_database(name, address):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, address) VALUES (%s, %s)", (name, address))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        save_user_to_database(name, address)
        return jsonify({'status': 'success', 'name': name, 'address': address})
    
    # For GET request, just show a simple form
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Address: <input type="text" name="address"><br>
            <input type="submit" value="Save">
        </form>
    '''

@app.route('/health')
def health_check():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return 'Application is up and running!', 200
    except Exception as e:
        return f'Health check failed: {e}', 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
