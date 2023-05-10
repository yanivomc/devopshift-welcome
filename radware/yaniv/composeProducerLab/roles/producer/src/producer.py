import os
import json
import random
import string
import time

import pika


# Set up logging - this is a comment
def log(message, level='debugging'):
    log_obj = {'level': level, 'timestamp': int(time.time()), 'message': message}
    print(json.dumps(log_obj))


# Generate random user information
def generate_user_info():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    first_name = ''.join(random.choices(string.ascii_uppercase, k=8))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=8))
    email = f'{username}@example.com'
    return {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email}


# Connect to RabbitMQ
rmq_host = os.environ.get('rmq_host', 'localhost')
rmq_port = os.environ.get('rmq_port', '5672')
rmq_user = os.environ.get('rmq_user', 'guest')
rmq_password = os.environ.get('rmq_password', 'guest')
rmq_topic = os.environ.get('rmq_topic', 'user_info')

credentials = pika.PlainCredentials(rmq_user, rmq_password)
parameters = pika.ConnectionParameters(host=rmq_host, port=rmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Publish messages
log('Starting message producer...')
while True:
    try:
        user_info = generate_user_info()
        message = json.dumps(user_info)
        channel.basic_publish(exchange='', routing_key=rmq_topic, body=message)
        log(f"Sent message: {message}")
    except Exception as e:
        log(f"Error sending message: {str(e)}", level='error')
    finally:
        time.sleep(1)

# Close connection
connection.close()
