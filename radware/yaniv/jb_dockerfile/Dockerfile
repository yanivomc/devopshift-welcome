FROM yanivomc/alpine-oraclejdk8:slim 
WORKDIR /app
COPY ./spring-music.jar ./spring-music.jar
EXPOSE 8080
CMD java -jar -Dspring.profiles.active=none spring-music.jar


# docker build -t IMAGE:TAG . 
# docker run -ti IMAGE:TAG
# docker run -d -p 80:8080 IMAGE:TAG