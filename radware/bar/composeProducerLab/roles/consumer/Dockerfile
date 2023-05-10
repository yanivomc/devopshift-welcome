# INSTRUCTIONS !!!
FROM  python:3.9-slim-buster
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV RMQ_HOST=localhost RMQ_PORT=5672 RMQ_USER=guest RMQ_PASSWORD=guest RMQ_TOPIC=user_info
COPY ./src/consumer.py ./consumer.py
CMD ["python", "consumer.py"]
