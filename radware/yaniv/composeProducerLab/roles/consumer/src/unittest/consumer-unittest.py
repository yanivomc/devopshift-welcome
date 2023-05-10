import unittest
import sqlite3
import pika
import json
import time
from consumer import callback, RMQ_QUEUE, conn

class TestConsumer(unittest.TestCase):

    def setUp(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RMQ_QUEUE)

        self.cursor = conn.cursor()
        self.cursor.execute('DELETE FROM user_info')
        conn.commit()

    def tearDown(self):
        self.connection.close()

    def test_callback(self):
        message = {
            'username': 'johndoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com'
        }
        self.channel.basic_publish(exchange='',
                                   routing_key=RMQ_QUEUE,
                                   body=json.dumps(message))

        time.sleep(1) # wait for message to be consumed and processed

        self.cursor.execute('SELECT COUNT(*) FROM user_info')
        count = self.cursor.fetchone()[0]

        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
