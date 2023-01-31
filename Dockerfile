FROM alpine:latest
RUN echo "pip install -f req.txt "
WORKDIR /code/
COPY ./anotherfile ./anotherfile.py
COPY ./testfile /code/testfile
EXPOSE 8080
ENTRYPOINT ["sleep" , "10" ]
