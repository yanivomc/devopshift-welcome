FROM  python:3.9-slim-buster
COPY /requirements.txt /requirements.txt
COPY /src/consumer.py /src/consumer.py
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/consumer.py"]
