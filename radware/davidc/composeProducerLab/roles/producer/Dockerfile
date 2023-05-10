# INSTRUCTIONS !!!
FROM  python:3.9-alpine
WORKDIR /app
COPY ./requirements.txt /app/req/requirements.txt
RUN pip install --no-cache-dir -r ./req/requirements.txt
COPY ./src/producer.py ./producer.py
CMD ["python", "producer.py"]
