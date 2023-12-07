FROM python:3.11
WORKDIR /app
COPY ./app.py /app
COPY ./req.txt /app
RUN pip install -r req.txt
CMD python app.py