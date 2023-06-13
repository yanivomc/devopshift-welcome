# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV MONGO_URL=mongodb://localhost:27017/
ENV MONGO_DB=nft_db
ENV MONGO_COLLECTION=nft_collection
ENV RMQ_URL=localhost
ENV DEBUG=True

# Run server.py when the container launches
CMD ["python", "server.py"]
