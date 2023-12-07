FROM yanivomc/simpleflask:latest
WORKDIR /app
COPY req.txt .
RUN pip install req.txt
COPY app.py .
CMD app.py