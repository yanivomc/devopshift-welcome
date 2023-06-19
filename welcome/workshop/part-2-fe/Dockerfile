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
ENV MONGO_HOST="mongodb://root:pass12345@mongo:27017/"
ENV MONGO_DB=nft_db
ENV MONGO_COLLECTION=nft_collection
ENV RMQ_HOST=rmq
ENV DEBUG=True
### DISABLE RMQ AND MONGO for im mem 
ENV DEBUG_RMQ = False 
ENV DEBUG_MONGO = False

# Run server.py when the container launches
CMD ["python", "server.py"]
