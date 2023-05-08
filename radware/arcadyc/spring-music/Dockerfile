FROM python:3.10.11-alpine3.17
WORKDIR /mycode
COPY ./myapp.py ./myapp.py
ENV DEFAULT_DB=MYSQL
ENV DB=MYSQL1
EXPOSE 8080
EXPOSE 8081
EXPOSE 8083
CMD [ "python", "myapp.py" ]