FROM python:alpine3.10 as base
COPY ./server.py /app/server.py
RUN echo "Running unit test"
WORKDIR /app
RUN python server.py