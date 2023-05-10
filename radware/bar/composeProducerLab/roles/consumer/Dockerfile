# INSTRUCTIONS !!!
FROM  python:3.9-slim-buster
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/consumer.py ./consumer.py
CMD ["python", "consumer.py"]
