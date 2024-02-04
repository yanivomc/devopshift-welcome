1. Please run docker compose commands below and watch the logs to allow all brokers to bootstrap and change state to RUNNING.
 ~~~
 docker compose up -d

 docker compose ps --services --filter "status=running"
 
 docker compose logs -f 
 ~~~ 
  
2. Once kafka is up and running please validate functionailty by running the following:

Create an example topic:
~~~
docker exec -it kafka1 /bin/bash
kafka-topics --bootstrap-server kafka1:9092 --create --topic exampleTopic
# Output:
Created topic exampleTopic.
# To exit the container, please specify exit
~~~

Produce messages:
~~~
docker exec -it kafka2 /bin/bash
kafka-console-producer --bootstrap-server kafka2:9092 --topic exampleTopic
>codersee
>rules 
# To exit the producer, please hit Ctrl + D. Then to exit the container please type 'exit'.
~~~

Consume messages:
~~~
docker exec -it kafka3 /bin/bash
kafka-console-consumer --bootstrap-server kafka3:9092 --topic exampleTopic --from-beginning
# Output:
codersee
rules
# To exit the consumer, please hit Ctrl + C. As the output, we should see:
^CProcessed a total of 2 messages
# And again, to exit the container please type 'exit'.
~~~


3. With the compose file running, we also got KAFKA conduktor installed (Free version),
To manage our kafka cluster.

Access Conduktor: http://REMOTEIP:8080

User: admin@admin.io
Password: admin

