from confluent_kafka import Producer
import consul
import json
import fastavro
from src.schemaManager import avroManager
from src.logger import JsonLogger

logger = JsonLogger(debug=True)

class KafkaProducer:
    def __init__(self, consul_host='localhost', consul_port=8500, consul_key='producer/kafka/configuration'):
        self.consul = consul.Consul(host=consul_host, port=consul_port)
        self.consul_key = consul_key
        self.config = None
        self.topic = None
        self.producer = None
        self.schema = None
        self.registryServers = None
        self.read_config_from_consul()

    def read_config_from_consul(self):
        # Here you would connect to Consul and read the configuration
        index = None
        while True:
            index, data = self.consul.kv.get(self.consul_key, index=index)
            if data is None:
                # The key doesn't exist, so we create it with a default value
                default_config = {
                    'topic': 'sold_nft_ex',
                    "registry.servers": "http://localhost:8081",
                    "kafkaConfig": {
                        "bootstrap.servers": "localhost:19092",
                        "client.id": "my_client_id",
                        "default.topic.config": {
                            "acks": "all"
                        }
                    },
                    'avro_schema': {
                        "type": "record",
                        "name": "Transaction",
                        "fields": [
                            {"name": "trx_status", "type": "string"},
                            {"name": "trx_id", "type": "string"},
                            {"name": "clientname", "type": "string"},
                            {"name": "nftid", "type": "string"},
                            {"name": "nftprice", "type": "float"},
                            {"name": "nftimage_url", "type": "string"}
                        ]
                    }
                }
                self.consul.kv.put(self.consul_key, json.dumps(default_config))
            else:
                new_config = json.loads(data['Value'].decode('utf-8'))
                logger.log({"message": "New configuration pulled from Consul", "Config": new_config, "module":"KafkaProducer", "type":'DEBUG'},level='debug')
                if new_config != self.config:
                    self.config = new_config
                    self.topic = self.config['topic']
                    self.registryServers = self.config['registry.servers']
                    self.producer = Producer(self.config['kafkaConfig'])
                    self.schema = fastavro.parse_schema(self.config['avro_schema'])
                    registryUpadte = avroManager(registryUrl=self.registryServers,topicName=self.topic,avroSchema=self.schema)
                    registryUpadte.manageRegistry()
                    
                    # Log a message about the successful configuration update

    def validate_message(self, message):
        # Here you would use the Avro schema to validate the message
        return fastavro.validate(message, self.schema)

    def produce_message(self, message):
        if not self.validate_message(message):
            # Log a message about the validation failure
            return
        self.producer.produce(self.topic, value=message)
        self.producer.flush()
