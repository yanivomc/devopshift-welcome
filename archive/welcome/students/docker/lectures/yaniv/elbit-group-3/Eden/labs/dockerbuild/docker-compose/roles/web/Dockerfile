FROM yanivomc/alpine-oraclejdk8:slim
WORKDIR /roles/web
COPY ./spring-music.jar /roles/web/spring-music.jar
EXPOSE 8080
CMD java -jar -Dspring.profiles.active=mysql /roles/web/spring-music.jar
