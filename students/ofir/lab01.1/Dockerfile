FROM python:3

WORKDIR /app

COPY app.py ./
COPY req.txt ./

RUN pip install -r req.txt

CMD ["python", "app.py"]

