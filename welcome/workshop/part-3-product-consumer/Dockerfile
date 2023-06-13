# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV RMQ_HOST=mongodb://localhost:27017/
ENV RMQ_QUEUE=queue_name
ENV RMQ_QUEUE_DLX=dead-letter-sold-nfts
ENV RMQ_QUEUE_MV=sold-nfts-mv
# MYSQL
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=username
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=db_name

# Run server.py when the container launches
CMD ["python", "server.py"]
