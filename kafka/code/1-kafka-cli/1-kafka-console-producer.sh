
kafka-console-producer 

# producing
kafka-console-producer --broker-list kafka1:9092 --topic first_topic 

# producing with properties
kafka-console-producer --broker-list kafka1:9092 --topic first_topic --producer-property acks=all

