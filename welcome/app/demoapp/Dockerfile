FROM python:3.7 as base
COPY ./server.py /app/server.py
RUN echo "Running unit test"
WORKDIR /app
RUN python server.py