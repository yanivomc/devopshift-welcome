import os
import json
import pika
import sqlite3

# Set up the RabbitMQ connection
rmq_host = os.environ.get("RMQ_HOST", "localhost")
rmq_port = os.environ.get("RMQ_PORT", "5672")
rmq_user = os.environ.get("RMQ_USER", "guest")
rmq_password = os.environ.get("RMQ_PASSWORD", "guest")
rmq_topic = os.environ.get("RMQ_TOPIC", "user_info")

credentials = pika.PlainCredentials(rmq_user, rmq_password)
parameters = pika.ConnectionParameters(rmq_host, rmq_port, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Set up the SQLite database connection
conn = sqlite3.connect("user_info.db")
c = conn.cursor()

# Create the user_info table if it doesn't exist
c.execute("""CREATE TABLE IF NOT EXISTS user_info (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                email TEXT
             )""")
conn.commit()

# Define the RabbitMQ message consumer callback
def callback(ch, method, properties, body):
    # Decode the message body from JSON
    data = json.loads(body)

    # Insert the message data into the user_info table
    c.execute("""INSERT INTO user_info (username, first_name, last_name, email)
                  VALUES (?, ?, ?, ?)""",
              (data["username"], data["first_name"], data["last_name"], data["email"]))
    conn.commit()

    # Send an acknowledgement to RabbitMQ
    channel.basic_ack(delivery_tag=method.delivery_tag)


# Start consuming messages from RabbitMQ
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=rmq_topic, on_message_callback=callback)

print("Consumer started. Waiting for messages...")
channel.start_consuming()
