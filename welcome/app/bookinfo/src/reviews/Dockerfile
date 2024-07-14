# Build Stage
FROM gradle:8.6.0-jdk8 AS builder

# Not sure why but we need root to build. Ignore lint error, this is for a multistage builder so it doesn't matter.
# hadolint ignore=DL3002
USER 0
COPY ./src/ /home/gradle

RUN gradle build

# Security Stage
FROM builder AS security
USER root
RUN apt-get update && apt-get install -y npm && rm -rf /var/lib/apt/lists/*
RUN curl --compressed https://static.snyk.io/cli/latest/snyk-linux?_gl=1*82pq22*_ga*MTY0ODQ2NTg4Ni4xNzIwOTUxOTcz*_ga_X9SH3KP7B4*MTcyMDk1MTk3My4xLjEuMTcyMDk1MTk3My42MC4wLjA -o ./snyk
RUN chmod +x ./snyk
COPY ./snyk /usr/local/bin/
# https://app.snyk.io/account - Register with a free account to generate authkey and use it as part of the CI , docker build ARG below-   generate link: https://app.snyk.io/account
ARG SNYK_TOKEN
ENV SNYK_TOKEN=${SNYK_TOKEN}
RUN ./snyk test /home/gradle/ --all-sub-projects

# Run Stage
FROM open-liberty:24.0.0.1-kernel-slim-java17-openj9

ENV SERVERDIRNAME reviews

# Copy built artifacts from the builder stage
COPY --from=builder /home/gradle/reviews-wlpcfg/servers/LibertyProjectServer/ /opt/ol/wlp/usr/servers/defaultServer/

RUN /opt/ol/wlp/bin/featureUtility installServerFeatures --acceptLicense /opt/ol/wlp/usr/servers/defaultServer/server.xml --verbose && \
    chmod -R g=rwx /opt/ol/wlp/output/defaultServer/

ARG service_version
ARG enable_ratings
ARG star_color
ENV SERVICE_VERSION=${service_version:-v1}
ENV ENABLE_RATINGS=${enable_ratings:-false}
ENV STAR_COLOR=${star_color:-black}

CMD ["/opt/ol/wlp/bin/server", "run", "defaultServer"]
