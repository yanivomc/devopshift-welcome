# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app
# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
ADD . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV CONSULHOST='consul'
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
ENV KAFKABROKER=kafka1
ENV KAFKAREGISTRY=kafka-schema-registry
WORKDIR /app/src

# Run server.py when the container launches
CMD ["flask" ,"run"]
