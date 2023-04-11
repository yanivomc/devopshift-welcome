# list topics
kafka-topics --bootstrap-server kafka1:9092 --list

# create a topic that we'll configure
kafka-topics --bootstrap-server kafka1:9092 --create --topic configured-topic --partitions 3 --replication-factor 1

# look for existing configurations
kafka-topics --bootstrap-server kafka1:9092 --describe --topic configured-topic

# documentation of kafka-configs command
kafka-configs

# Describe configs for the topic with the command
kafka-configs --bootstrap-server kafka1:9092 --entity-type topics --entity-name configured-topic --describe

# add a config to our topic
kafka-configs --bootstrap-server kafka1:9092 --entity-type topics --entity-name configured-topic --add-config min.insync.replicas=2 --alter

# Describe configs using kafka-configs
kafka-configs --bootstrap-server kafka1:9092 --entity-type topics --entity-name configured-topic --describe

# Describe configs using kafka-topics
kafka-topics --bootstrap-server kafka1:9092 --describe --topic configured-topic

# Delete a config
kafka-configs --bootstrap-server kafka1:9092 --entity-type topics --entity-name configured-topic --delete-config min.insync.replicas --alter

# ensure the config has been deleted
kafka-topics --bootstrap-server kafka1:9092 --describe --topic configured-topic