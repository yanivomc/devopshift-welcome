
### KAFKA PLAYGROUND
Welcome to Kafka playground.

Once your terminal is available,
Allow a few moments for your Kafka environments to bootstrap.

**You can follow the status of the process by running:**

    tail -f /var/log/user-data.log

  **Once you see output similar to the following:**
  

> Container kafka-connect  Started \
Container docker-compose-conduktor-1  Starting \
Container docker-compose-conduktor-1  Started 

**You may break the tail command and validate all services are running by executing:**

    cd /home/ubuntu/workarea/devopshift/kafka/docker-compose
    docker compose ps --services --status running | awk '{ print "Service:", $1, "is running" }'
    docker compose ps --services --status exited  | awk '{ print "Service:", $1, "exit" }'

Validate that all containers are up and no exited services.

> Service: conduktor is running
Service: connect-consumer is running \
Service: connect-datagen is running \
Service: datagen-ratings is running \
Service: kafka-connect is running \
Service: kafka-rest-proxy is running \
Service: kafka-schema-registry is running \
Service: kafka1 is running \
Service: kafka2 is running \
Service: kafka3 is running \
Service: ksqldb-server is running \
Service: mysql-db is running \
Service: phpmyadmin is running 

**To restart** kafka services you may run:

    docker compose restart
---

### Accessing Kafka
Once all services are up,
you may access **KAFKA brokers directly** or using **conduktor**

**Option 1:** Accessing Kafka brokers (kafka1 - kafka3):

    docker exec -ti kafka1 bash
**Option 2:** Run the following command for accessing conduktor:

    echo "Your conduktor URL is: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):8080"

Username: admin@admin.io \
Password:  admin
