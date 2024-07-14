# Build Stage
FROM node:21.6-slim AS build

# Install curl
RUN apt-get update \
    && apt-get install curl --no-install-recommends -y \
    && rm -rf /var/lib/apt/lists/*

ARG service_version
ENV SERVICE_VERSION ${service_version:-v1}

COPY package.json /opt/microservices/
WORKDIR /opt/microservices
RUN npm install

# Lint/Test Stage
FROM build AS lint-test

# Create ESLint configuration file
COPY ratings.js /opt/microservices/
RUN npm install eslint --save-dev
COPY eslint.config.js /opt/microservices/eslint.config.js
RUN npx eslint /opt/microservices/ratings.js

# Run Stage
FROM node:21.6-slim AS run

WORKDIR /opt/microservices

# Copy the necessary files from the build stage
COPY --from=build /opt/microservices /opt/microservices
COPY ratings.js /opt/microservices/

EXPOSE 9080

CMD ["node", "/opt/microservices/ratings.js", "9080"]

USER 1000
