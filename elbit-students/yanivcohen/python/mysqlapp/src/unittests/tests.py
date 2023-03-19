import mysql.connector
import hashlib
import random
import datetime
import unittest
import os

# Get env from OS
db_endpoint = os.getenv('DB-ENDPOINT', default='localhost')
# Set variables
# db_endpoint = 'localhost'
db_name = 'mydatabase'
db_table = 'mytable'
db_user = 'root'
db_password = 'mydatabase'

class TestDB(unittest.TestCase):
    
    def setUp(self):
        # Connect to database
        self.mydb = mysql.connector.connect(
            host=db_endpoint,
            user=db_user,
            password=db_password
        )
        
        # Check if database exists and create it if it doesn't
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.mycursor.execute(f"USE {db_name}")
        
        # Check if table exists and create it if it doesn't
        self.mycursor.execute(f"CREATE TABLE IF NOT EXISTS {db_table} (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, hash_value VARCHAR(255))")
        
    def test_table_exists(self):
        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchall()
        table_names = [table[0] for table in tables]
        self.assertIn(db_table, table_names)
        
    def test_write_hashes(self):
        for i in range(10):
            date = datetime.datetime.now().date()
            hash_value = hashlib.sha256(str(random.randint(0, 100000)).encode('utf-8')).hexdigest()
            sql = f"INSERT INTO {db_table} (date, hash_value) VALUES (%s, %s)"
            val = (date, hash_value)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            self.assertEqual(self.mycursor.rowcount, 1)
        
    def tearDown(self):
        # Delete test data from table
        self.mycursor.execute(f"DELETE FROM {db_table}")
        self.mydb.commit()
        self.mydb.close()

if __name__ == '__main__':
    unittest.main()
