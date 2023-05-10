FROM python:3.9-slim-buster
WORKDIR /consumer
COPY ./src/*.txt ./. 
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/*.py ./.

CMD python consumer.py