# שלב 1: התקנת התלויות
FROM python:3.12.1-slim AS build

WORKDIR /app

# להעתיק את קובצי הדרישות
COPY requirements.txt ./
COPY test-requirements.txt ./
RUN pip3 install -vvv --require-hashes --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir --require-hashes -r test-requirements.txt

# שלב 2: בניית האפליקציה
FROM python:3.12.1-slim

WORKDIR /app

# להעתיק את התלויות מהשלב הקודם
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# להעתיק את קובצי האפליקציה
COPY productpage.py /opt/microservices/
COPY tests/unit /opt/microservices/tests/unit
COPY templates /opt/microservices/templates
COPY static /opt/microservices/static
COPY requirements.txt /opt/microservices/

# להגדיר את המשתנים והפקודות
ARG flood_factor
ENV FLOOD_FACTOR ${flood_factor:-0}

EXPOSE 9080
WORKDIR /opt/microservices
RUN python -m unittest discover

CMD ["gunicorn", "-b", "[::]:9080", "productpage:app", "-w", "8", "--keep-alive", "2", "-k", "gevent"]

USER 1000
