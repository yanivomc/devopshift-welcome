import mysql.connector
import hashlib
import random
import datetime

# Set variables
db_endpoint = 'localhost'
db_name = 'mydatabase'
db_table = 'mytable'
db_user = 'myusername'
db_password = 'mypassword'

# Connect to database
mydb = mysql.connector.connect(
  host=db_endpoint,
  user=db_user,
  password=db_password
)

# Check if database exists and create it if it doesn't
mycursor = mydb.cursor()
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
mycursor.execute(f"USE {db_name}")

# Check if table exists and create it if it doesn't
mycursor.execute(f"CREATE TABLE IF NOT EXISTS {db_table} (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, hash_value VARCHAR(255))")

# Write random hashes to table
for i in range(10):
    date = datetime.datetime.now().date()
    hash_value = hashlib.sha256(str(random.randint(0, 100000)).encode('utf-8')).hexdigest()
    sql = f"INSERT INTO {db_table} (date, hash_value) VALUES (%s, %s)"
    val = (date, hash_value)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
