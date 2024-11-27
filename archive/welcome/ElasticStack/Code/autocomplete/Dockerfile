# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Elasticsearch Python clients
RUN pip install -r requirements.txt

# Specify the command to run on container start
CMD ["python", "server.py"]
