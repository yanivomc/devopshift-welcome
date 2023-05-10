FROM yanivomc/alpine-oraclejdk8:slim 
WORKDIR /code
COPY ./spring-music.jar /code/spring-music.jar
EXPOSE 8080
CMD java -jar -Dspring.profiles.active=mysql /code/spring-music.jar

# docker build -t mayimg:01 .
# docker run -d -p 80:8080 mayimg:01