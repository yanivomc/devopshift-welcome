{
    "name": "mysql-source",
    "config": {
        "connector.class": "io.debezium.connector.mysql.MySqlConnector",  # Specifies the connector class for Debezium's MySQL Connector
        "database.hostname": "mysql-db",  # Specifies the hostname of the MySQL database to connect to
        "database.port": "3306",  # Specifies the port number of the MySQL database
        "database.user": "root",  # Specifies the username to use for authenticating with the MySQL database
        "database.server.id": "1",  # Specifies a unique ID for the MySQL server, used for generating globally unique transaction IDs
        "database.server.name": "mysql1",  # Specifies a unique name for the MySQL server, used for generating Kafka topics
        "database.whitelist": "accounts",  # Specifies the MySQL database(s) to capture data from
        "table.whitelist": "users-accounts",  # Specifies the MySQL table(s) to capture data from
        "topic.prefix": "mydb-",  # Specifies a prefix to prepend to the generated Kafka topic names
        "database.history.kafka.bootstrap.servers": "kafka1:19092",  # Specifies the Kafka broker(s) to use for storing database schema history
        "database.history.kafka.topic": "dbhistory.mysql",  # Specifies the name of the Kafka topic to use for storing database schema history
        "transforms": "unwrap",  # Specifies the set of transformations to apply to the data, in this case just the "unwrap" transformation
        "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",  # Specifies the transformation to use for extracting the new record state
        "transforms.unwrap.drop.tombstones": "false",  # Specifies whether to include or exclude Kafka tombstone messages when extracting record states
        "schema.history.kafka.bootstrap.servers": "kafka1:19092",  # Specifies the Kafka broker(s) to use for storing connector-specific schema history
        "schema.history.kafka.topic": "mysql-history",  # Specifies the name of the Kafka topic to use for storing connector-specific schema history
        "schema.history.internal.kafka.topic": "mysql-history",  # Specifies the name of the Kafka topic to use for storing internal connector-specific schema history
        "schema.history.internal.kafka.bootstrap.servers": "kafka1:19092"  # Specifies the Kafka broker(s) to use for storing internal connector-specific schema history
    }
}
