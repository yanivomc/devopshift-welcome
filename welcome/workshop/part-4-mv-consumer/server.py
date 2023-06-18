import os
import sys
import pika
import json
from pymongo import MongoClient # to connect to MongoDB
import logging

DEBUG=os.environ.get('DEBUG', 'True').lower() == 'true'
# RabbitMQ Configuration
RMQ_HOST = os.getenv("RMQ_HOST", "localhost")
print(RMQ_HOST)
RMQ_QUEUE = os.getenv("RMQ_QUEUE", "sold-nft")
RMQ_QUEUE_DLX = os.getenv("RMQ_QUEUE_DLX", "dead-letter-sold-nfts")
RMQ_QUEUE_MV = os.getenv("RMQ_QUEUE_MV", "sold-nfts-mv")
RMQ_EXCHANGE = os.getenv("RMQ_EXCHANGE", "sold_nft_ex")
RMQ_USERNAME = os.getenv("RMQ_USERNAME", "guest")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD", "123456")

# MongoDB Configuration
MONGO_HOST = os.getenv("MONGO_HOST","mongodb://root:pass12345@localhost:27017/")

DEBUG_RMQ = os.environ.get('DEBUG_RMQ', False)
DEBUG_MONGO = os.environ.get('DEBUG_MONGO', False)

# Mongo Configuration
if not DEBUG_MONGO == True:
    print(MONGO_HOST)
    client = MongoClient(MONGO_HOST)
    # check if the database 'nft_db' exists
if 'nft_db' not in client.list_database_names():
    # if not, create it by inserting a document
    client['nft_db']['temp'].insert_one({'temp': 'temp'})
    # and then immediately delete the document
    client['nft_db']['temp'].delete_one({'temp': 'temp'})
    print("Database 'nft_db' created.")
else:
    print("Database 'nft_db' already exists.")

# use the 'nft_db' database
db = client['nft_db']

# check if the collection 'nft_collections' exists
if 'nft_collections' not in db.list_collection_names():
    # if not, create it by inserting a document
    db['nft_collections'].insert_one({'temp': 'temp'})
    # and then immediately delete the document
    db['nft_collections'].delete_one({'temp': 'temp'})
    print("Collection 'nft_collections' created.")
else:
    print("Collection 'nft_collections' already exists.")
    
# check if the collection 'sold_nfts_mv_collections' exists
if 'sold_nfts_mv_collections' not in db.list_collection_names():
    # if not, create it by inserting a document
    db['sold_nfts_mv_collections'].insert_one({'temp': 'temp'})
    # and then immediately delete the document
    db['sold_nfts_mv_collections'].delete_one({'temp': 'temp'})
    print("Collection 'sold_nfts_mv_collections' created.")
else:
    print("Collection 'sold_nfts_mv_collections' already exists.")    
    
    db = client['nft_db'] # replace 'nft_db' with your MongoDB database name
    nft_collection = db['sold_nfts_mv_collections'] # replace 'nft_collection' with your MongoDB collection name

# Logging Configuration
logging.basicConfig(level=logging.DEBUG if DEBUG == True else logging.INFO)

# Message validation
REQUIRED_KEYS = {"trx_status", "trx_id","clientname", "nftid", "nftprice", "nftimage_url"}



if not DEBUG_RMQ==True:
    # RabbitMQ Connection
    credentials = pika.PlainCredentials(RMQ_USERNAME, RMQ_PASSWORD)
    parameters = pika.ConnectionParameters(host=RMQ_HOST, credentials=credentials)
    rmq_connection = pika.BlockingConnection(parameters)
    # rmq_connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST))
    rmq_channel = rmq_connection.channel()


def handle_message(ch, method, properties, body):
    logging.debug(f"Received {body}")

    # Parse and validate message
    try:
        message = json.loads(body)
        if not REQUIRED_KEYS.issubset(message):
            raise ValueError("Missing required keys")
        if any(not message[key] for key in REQUIRED_KEYS):
            raise ValueError("One or more keys have empty values")
    
        if not DEBUG_MONGO==True:
            # Save to MongoDB
            document = {
                "_id": message["trx_id"],
            }
            for key, value in message.items():
                document[key] = value
                
            # update or insert the document
            nft_collection.update_one({'_id': document['_id']}, {'$set': document}, upsert=True)

        # Acknowledge message after successful processing
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        logging.error(f"Failed to process message: {e}")
        rmq_channel.basic_publish(
            exchange="",
            routing_key=RMQ_QUEUE_DLX,
            body=body,
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
    




def init_rmq_mongo():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST))
    # channel = connection.channel()

    if not DEBUG_RMQ==True:
        # Create RMQ queue if not exists
        try:
            rmq_channel.exchange_declare(exchange_type="direct",exchange=RMQ_EXCHANGE)
            rmq_channel.queue_declare(queue=RMQ_QUEUE_DLX)
            rmq_channel.queue_declare(queue=RMQ_QUEUE_MV)
            rmq_channel.queue_bind(exchange=RMQ_EXCHANGE, queue=RMQ_QUEUE, routing_key='')
            rmq_channel.queue_bind(exchange=RMQ_EXCHANGE, queue=RMQ_QUEUE_MV, routing_key='')
        except Exception as e:
            if DEBUG:
                print(f"Failed to create RMQ queue: {e}")
            sys.exit(1)
    if not DEBUG_MONGO==True:
        # Create MySQL table if not exists
        pass

    if not DEBUG_RMQ==True:            
        rmq_channel.basic_qos(prefetch_count=1)
        rmq_channel.basic_consume(queue=RMQ_QUEUE_MV, on_message_callback=handle_message, auto_ack=False)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        rmq_channel.start_consuming()


if __name__ == "__main__":
    # logging.root.setLevel(logging.DEBUG)
    init_rmq_mongo()
    # Rest of the script...
