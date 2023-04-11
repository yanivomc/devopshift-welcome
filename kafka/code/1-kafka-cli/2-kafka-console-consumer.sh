kafka-console-consumer 

# consuming
kafka-console-consumer --bootstrap-server kafka1:9092 --topic first_topic

# other terminal
kafka-console-producer --broker-list kafka1:9092 --topic first_topic

# consuming from beginning
kafka-console-consumer --bootstrap-server kafka1:9092 --topic first_topic --from-beginning