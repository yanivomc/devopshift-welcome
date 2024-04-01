from confluent_kafka import Consumer, KafkaError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Confluent Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'kafka1:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'latest',
    'enable.auto.commit': False,
}

# Create Confluent Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to topic
consumer.subscribe(['configured-topic'])

# Start consuming messages
try:
    while True:
        msg = consumer.poll(1.0)  # Poll for a message with a 1-second timeout

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                continue
            else:
                logging.error(msg.error())
                break

        # Process message
        logging.info('Message consumed: %s' % msg.value().decode('utf-8'))

        # Commit offset
        consumer.commit(asynchronous=False)

        # Log committed offset
        logging.info('Offset committed for offset: %s' % msg.offset())

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer to commit any remaining offsets and release resources
    consumer.close()
