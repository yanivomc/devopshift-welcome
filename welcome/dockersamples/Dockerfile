# STAGE BUILD
FROM python:3.11.10-alpine3.20 AS BUILD
COPY ./src/demo.java /code/demo.java
CMD ["echo","javac ....."] ## > /code/src...../demo.jar

FROM java/securiy:latest AS SEC
COPY --from=BUILD /code/src/demo.jar /code/test/demo.jar

