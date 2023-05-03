import mysql.connector
from faker import Faker
import time

fake = Faker()

# connect to database
mydb = mysql.connector.connect(
  host="mysql-db",
  user="root",
  database="accounts"
)

# create table if not exists
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users_accounts (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), username VARCHAR(255))")

# generate and insert fake data
count = 0
while True:
  first_name = fake.first_name()
  last_name = fake.last_name()
  email = fake.email()
  username = (first_name + last_name).lower()

  sql = "INSERT INTO users_accounts (first_name, last_name, email, username) VALUES (%s, %s, %s, %s)"
  val = (first_name, last_name, email, username)
  mycursor.execute(sql, val)

  count += 1
  if count % 10 == 0:
    print(f"{count} rows inserted")
    mydb.commit()
    time.sleep(0.3)

# commit changes and close connection
mycursor.close()
mydb.close()
