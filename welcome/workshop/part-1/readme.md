

**Task 1: Building the Application Diagram**

Your task is to design an architecture diagram for a Python-based application. This application is built around several interconnected services. Here are the requirements for each component:

1. **Flask Frontend**: This is the user-facing portion of the application. It communicates with the MongoMicroFrontendReader to read data. Additionally, it sends new product descriptions to the ProductConsumer via RMQ (RabbitMQ).

2. **MongoMicroFrontendReader**: This service is responsible for reading data from MongoDB and making it available to the Flask Frontend.

3. **MongoDB**: This acts as both the event source and CQRS (Command Query Responsibility Segregation) for the application.

4. **RMQ (RabbitMQ)**: RMQ has two responsibilities. First, it operates a queue called `products` which facilitates communication between the Flask Frontend and the ProductConsumer. Second, it operates another queue called `PRODUCT-EVENTSOURCE` which is used to send data from the ProductConsumer to the EventSource Consumer.

5. **ProductConsumer**: This service reads data from the `products` queue in RMQ, saves it to a MySQL DB, and, upon receiving an acknowledgement from MySQL, sends the data to the `PRODUCT-EVENTSOURCE` queue in RMQ.

6. **MySQL DB**: The ProductConsumer stores product data here.

7. **EventSource Consumer**: This service consumes data from the `PRODUCT-EVENTSOURCE` queue in RMQ and writes it to MongoDB, making the data available to the Flask Frontend via the MongoMicroFrontendReader.

Your job is to take these requirements and build a comprehensive architecture diagram. Be sure to show how data flows between components and how each service interacts with others. Once your diagram is complete, compare it with your peers to see different approaches to the same task. 

Remember, there's no one 'correct' way to build this diagram. The goal is to understand the role and interaction of each component within the system.

Good luck!