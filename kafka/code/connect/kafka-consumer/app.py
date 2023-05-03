from kafka import KafkaConsumer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Kafka Consumer configuration
conf = {
    'bootstrap_servers': ['kafka1:9092'],
    'group_id': 'mygroup',
    'auto_offset_reset': 'latest',
    'enable_auto_commit': False
}

# Create Kafka consumer instance
consumer = KafkaConsumer('mydb-.accounts.users_accounts', **conf)

# Start consuming messages
try:
    while True:
        for msg in consumer:
            # Process message
            logging.info('Message consumed: %s' % msg.value)

            # Commit offset
            consumer.commit()

            # Log committed offset
            logging.info('Offset committed: %s' % msg.offset)

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer to commit any remaining offsets and release resources
    consumer.close()
