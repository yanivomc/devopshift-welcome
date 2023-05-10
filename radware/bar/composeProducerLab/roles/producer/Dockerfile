# INSTRUCTIONS !!!
FROM  python:3.9-alpine
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/producer.py ./user_info_producer.py
CMD ["python", "user_info_producer.py"]
