FROM python:3.8-slim-bullseye AS builder
COPY ./src /code
RUN sleep 5
WORKDIR /code
COPY ./requirements.txt ./requirements.txt

FROM python:3.9.18-slim-bullseye AS unitest
COPY --from=builder /code /unitest
WORKDIR /unitest
RUN pip install -r requirements.txt
RUN python unit_test.py


FROM python:3.8-slim-bullseye AS deploy
COPY --from=unitest /unitest /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python server.py
