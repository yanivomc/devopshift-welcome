# INSTRUCTIONS !!!
FROM  python:3.9-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/req/requirements.txt
RUN pip install --no-cache-dir -r ./req/requirements.txt
COPY ./src/consumer.py ./consumer.py
CMD ["python", "consumer.py"]
