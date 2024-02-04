#!/bin/sh

sed -i '/KAFKA_ZOOKEEPER_CONNECT/d' /etc/confluent/docker/configure

sed -i 's/cub zk-ready/echo ignore zk-ready/' /etc/confluent/docker/ensure

echo "kafka-storage format --ignore-formatted -t NqnEdODVKkiLTfJvqd1uqQ== -c /etc/kafka/kafka.properties" >> /etc/confluent/docker/ensure



# The first line is responsible for turning off the check for the KAFKA_ZOOKEEPER_CONNECT parameter. Without this line, the error will be thrown: Command [/usr/local/bin/dub ensure KAFKA_ZOOKEEPER_CONNECT] FAILED !

# The second line ignores the cub zk-ready. Without it, everything will end up with another exception: zk-ready: error: too few arguments.




# And finally, the last line is a KRaft required step, which formats the storage directory with a new cluster identifier. Please keep in mind that the specified UUID value (NqnEdODVKkiLTfJvqd1uqQ== in my case) has to be 16 bytes of a base64-encoded UUID.

