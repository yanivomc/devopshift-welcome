

kafka-topics 

kafka-topics --bootstrap-server kafka1:9092 --list 

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --create

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --create --partitions 3

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --create --partitions 3 --replication-factor 2

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --create --partitions 3 --replication-factor 1

kafka-topics --bootstrap-server kafka1:9092 --list 

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --describe

kafka-topics --bootstrap-server kafka1:9092 --topic first_topic --delete