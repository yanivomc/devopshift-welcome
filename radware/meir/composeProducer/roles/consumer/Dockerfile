FROM python:3.9-slim-buster
WORKDIR /consumer
COPY ./src ./
RUN pip install --no-cache-dir -r requirements.txt
CMD python consumer.py