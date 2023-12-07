FROM python:3.11.7-slim
WORKDIR /app
COPY ./app.py ./
COPY ./req.txt ./
RUN pip install -r req.txt
CMD python app.py