FROM yanivomc/alpine-oraclejdk8:slim
RUN echo "This is my first image"
WORKDIR /app
COPY spring-music.jar ./
EXPOSE 8080
CMD ["java", "-jar" , "-Dspring.profiles.active=none", "spring-music.jar"]