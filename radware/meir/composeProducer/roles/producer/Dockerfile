FROM python:3.9-alpine
WORKDIR /prod
COPY ./src/requirements.txt . 
RUN pip install --no-cache-dir -r ./requirements.txt
COPY ./src/*.py ./.
CMD python producer.py