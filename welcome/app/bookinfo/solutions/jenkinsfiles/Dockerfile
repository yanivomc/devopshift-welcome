# Build REQUIREMENTS
FROM python:alpine3.10 as base
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Build TEST
FROM base as test
WORKDIR /app
COPY ./src/server.py /app/server.py
RUN echo "Running unit test"



# Build lint stage
FROM alpine:latest as lint
RUN echo "Running lint"



# Build PRODUCTION
FROM base as production
WORKDIR /app
COPY ./src/server.py /app/server.py
CMD [ "python", "server.py" ]
