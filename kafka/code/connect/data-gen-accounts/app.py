import mysql.connector
from faker import Faker
import random
import time

fake = Faker()

# Connect to the database
mydb = mysql.connector.connect(
  host="mysql-db",
  user="root",
  database="accounts"
)

# Create users_accounts table if not exists
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users_accounts (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), username VARCHAR(255), user_id VARCHAR(255) UNIQUE)")

# Create orders table if not exists
mycursor.execute("CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, userid VARCHAR(255), orderid VARCHAR(255), product VARCHAR(255), price FLOAT)")

# Corrected script snippet

# Generate and insert fake data
count = 0
total_orders_added = 0  # To keep track of total orders added
try:
    while True:
      first_name = fake.first_name()
      last_name = fake.last_name()
      email = fake.email()
      username = (first_name + last_name).lower()
      user_id = fake.uuid4()  # Generate a random UUID for each user

      # Insert user account data
      sql = "INSERT IGNORE INTO users_accounts (first_name, last_name, email, username, user_id) VALUES (%s, %s, %s, %s, %s)"
      val = (first_name, last_name, email, username, user_id)
      mycursor.execute(sql, val)

      # Generate and insert random number of orders for each user
      num_orders = random.randint(1, 5)
      for _ in range(num_orders):
        orderid = fake.uuid4()  # Generate a random UUID for each order
        product = fake.word()  # Generate a random product name
        price = round(random.uniform(100, 500), 2)  # Generate a random price between 100 and 500

        sql = "INSERT INTO orders (userid, orderid, product, price) VALUES (%s, %s, %s, %s)"
        val = (user_id, orderid, product, price)
        mycursor.execute(sql, val)
        total_orders_added += 1

      count += 1
      if count % 10 == 0:
        print(f"{count} users created with {total_orders_added} orders added")
        mydb.commit()  # Commit after every 10 users (and their orders) are inserted
        time.sleep(0.3)
finally:
    # Ensure that the cursor and connection are closed properly
    mycursor.close()
    mydb.close()