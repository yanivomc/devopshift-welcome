FROM yanivomc/alpine-oraclejdk8:slim
COPY spring-music.jar /app
EXPOSE 8090
CMD java -jar -Dspring.profiles.active=none spring-music.jar 