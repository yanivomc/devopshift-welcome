import os
import sys
import pika
import json
import mysql.connector
import logging


# RabbitMQ Configuration
RMQ_HOST = os.getenv("RMQ_HOST", "localhost")
RMQ_QUEUE = os.getenv("RMQ_QUEUE", "sold-nft")
RMQ_QUEUE_DLX = os.getenv("RMQ_QUEUE_DLX", "dead-letter-sold-nfts")
RMQ_QUEUE_MV = os.getenv("RMQ_QUEUE_MV", "sold-nfts-mv")
RMQ_USERNAME = os.getenv("RMQ_USERNAME", "guest")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD", "123456")

# MySQL Configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_USER = os.getenv("MYSQL_USER", "username")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_DB = os.getenv("MYSQL_DB", "db_name")

# Logging Configuration
logging.basicConfig(level=logging.DEBUG if os.getenv("DEBUG") == "true" else logging.INFO)

# Message validation
REQUIRED_KEYS = {"trx_status", "trx_id","clientname", "nftid", "nftprice", "nftimage_url"}

DEBUG_RMQ = os.environ.get('DEBUG_RMQ', False)
DEBUG_MYSQL = os.environ.get('DEBUG_MYSQL', True)

if not DEBUG_RMQ==True:
    # RabbitMQ Connection
    credentials = pika.PlainCredentials(RMQ_USERNAME, RMQ_PASSWORD)
    parameters = pika.ConnectionParameters(host=RMQ_HOST, credentials=credentials)
    rmq_connection = pika.BlockingConnection(parameters)
    # rmq_connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST))
    rmq_channel = rmq_connection.channel()

if not DEBUG_MYSQL==True:
    # MySQL Connection
    mysql_conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
    )
    mysql_cursor = mysql_conn.cursor()


def handle_message(ch, method, properties, body):
    logging.debug(f"Received {body}")

    # Parse and validate message
    try:
        message = json.loads(body)
        if not REQUIRED_KEYS.issubset(message):
            raise ValueError("Missing required keys")
        if any(not message[key] for key in REQUIRED_KEYS):
            raise ValueError("One or more keys have empty values")
        # Update body trx_status with status stored in PROCESSED
        message["trx_status"] = "Processed"
        if not DEBUG_MYSQL==True:
            # Save to MySQL
            mysql_cursor.execute(
                "INSERT INTO sold_nfts (trx_status,trx_id, clientname, nftid, nftprice, nftimage_url) VALUES (%s, %s, %s, %s)",
                (message["trx_status"],message["trx_id"],message["clientname"], message["nftid"], message["nftprice"], message["nftimage_url"]),
            )
            mysql_conn.commit()
            logging.debug("Saved to MySQL")

        # Publish to RMQ
        rmq_channel.basic_publish(
            exchange="",
            routing_key=RMQ_QUEUE_MV,
            body=json.dumps(message),
        )
        logging.debug("Published to RMQ")

        # Acknowledge message
        ch.basic_ack(delivery_tag=method.delivery_tag)
        logging.debug("Acknowledged message")

    except Exception as e:
        logging.error(f"Failed to process message: {e}")
        rmq_channel.basic_publish(
            exchange="",
            routing_key=RMQ_QUEUE_DLX,
            body=body,
        )
        ch.basic_nack(delivery_tag=method.delivery_tag)




def init_rmq_mysql():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST))
    # channel = connection.channel()

    if not DEBUG_RMQ==True:
        # Create RMQ queue if not exists
        try:
            rmq_channel.queue_declare(queue=RMQ_QUEUE)
            rmq_channel.queue_declare(queue=RMQ_QUEUE_DLX)
            rmq_channel.queue_declare(queue=RMQ_QUEUE_MV)
        except Exception as e:
            if DEBUG:
                print(f"Failed to create RMQ queue: {e}")
            sys.exit(1)
    if not DEBUG_MYSQL==True:
        # Create MySQL table if not exists
        cnx = mysql.connector.connect(user=MYSQL_USER, database=MYSQL_DB)
        cursor = cnx.cursor()
        table_create_query = f"""
        CREATE TABLE IF NOT EXISTS {'sold_nfts'} (
            trx_status VARCHAR(255),
            trx_id VARCHAR(255),
            clientname VARCHAR(255),
            nftid VARCHAR(255),
            nftprice FLOAT,
            nftimage_url VARCHAR(255)
        );
        """
        try:
            cursor.execute(table_create_query)
            cnx.commit()
        except Exception as e:
            if DEBUG_MYSQL:
                print(f"Failed to create MySQL table: {e}")
            sys.exit(1)
    if not DEBUG_RMQ==True:            
        rmq_channel.basic_consume(queue=RMQ_QUEUE, on_message_callback=handle_message, auto_ack=False)
        rmq_channel.start_consuming()


if __name__ == "__main__":
    logging.root.setLevel(logging.DEBUG)
    init_rmq_mysql()

