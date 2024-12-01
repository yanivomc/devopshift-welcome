# STAGE BUILD
FROM python:3.11.10-alpine3.20 AS builder
RUN echo 'this is builder im running build'
COPY ./src/hello.py /src/hello.py
CMD ["sleep","5"]


FROM python:3.11.10-alpine3.20 AS lint
RUN echo 'this is linting'
CMD ["sleep","2"]


FROM nginx:latest AS security
RUN echo 'this is security'
CMD ["sleep","2"]


# Generate RC
FROM ubuntu:latest AS rc
COPY --from=builder /src/hello.py /code/hello.py
RUN echo 'this is RC'
CMD ["sleep","90000"]