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
ENV RMQ_HOST=rmq
ENV RMQ_QUEUE=sold-nft
ENV RMQ_QUEUE_DLX=dead-letter-sold-nfts
ENV RMQ_QUEUE_MV=sold-nfts-mv
ENV MONGO_HOST="mongodb://root:pass12345@mongo:27017/"
# Run server.py when the container launches
CMD ["python", "server.py"]
