# Dockerfile for Frontend Service
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD ["python", "main.py"]

EXPOSE 5002