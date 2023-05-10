import os
import pika
import sqlite3
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RMQ_HOST = os.getenv('RMQ_HOST', 'localhost')
RMQ_PORT = os.getenv('RMQ_PORT', 5672)
RMQ_USERNAME = os.getenv('RMQ_USERNAME', 'guest')
RMQ_PASSWORD = os.getenv('RMQ_PASSWORD', 'guest')
RMQ_QUEUE = os.getenv('RMQ_QUEUE', 'user_info')

DB_PATH = os.getenv('DB_PATH', 'user_info.db')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=RMQ_HOST,
        port=RMQ_PORT,
        credentials=pika.PlainCredentials(
            username=RMQ_USERNAME,
            password=RMQ_PASSWORD,
        ),
    )
)
channel = connection.channel()

channel.queue_declare(queue=RMQ_QUEUE)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
''')
conn.commit()

def callback(ch, method, properties, body):
    logging.info('Message consumed: %s', body.decode())

    try:
        data = json.loads(body.decode())

        cursor.execute('''
            INSERT INTO user_info (username, first_name, last_name, email)
            VALUES (?, ?, ?, ?)
        ''', (data['username'], data['first_name'], data['last_name'], data['email']))
        conn.commit()

        logging.info('Message stored in database: OK')
    except Exception as e:
        logging.error('Error storing message in database: %s', str(e))

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=RMQ_QUEUE, on_message_callback=callback)

logging.info('Consumer started. Waiting for messages...')
channel.start_consuming()
