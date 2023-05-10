FROM python:3.9-alpine
WORKDIR /prod
COPY ./src ./
RUN pip install --no-cache-dir -r requirements.txt
CMD python producer.py