# Python 3.9 image that runs our server app
FROM python:3.9-slim
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY ./src /app
WORKDIR /app
CMD ["python", "server.py"]
