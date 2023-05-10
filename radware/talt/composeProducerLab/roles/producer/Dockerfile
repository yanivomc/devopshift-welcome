FROM  python:3.9-alpine
COPY /requirements.txt /requirements.txt
COPY /src/producer.py /src/producer.py
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/producer.py"]