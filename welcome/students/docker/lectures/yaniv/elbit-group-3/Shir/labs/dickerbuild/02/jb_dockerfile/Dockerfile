FROM yanivomc/a



WORKDIR /app
COPY ./spring-music.jar /app/
EXPOSE 8080
CMD java -jar -Dspring.profiles.active=none ./spring-music.jar
