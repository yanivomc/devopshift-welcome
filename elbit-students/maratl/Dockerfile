FROM maratl/alpine-oracle.jdk8:slim
WORKDIR /app
COPY spring-music.jar /app
EXPOSE 8080
CMD java -jar -Dspring.profiles.active=none spring-music.jar
