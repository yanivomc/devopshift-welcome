FROM python:3.12.0-slim
WORKDIR /code
RUN pip install confluent_kafka
COPY ./app.py /code/
CMD ["sleep","900000"]