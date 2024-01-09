# Multi-stage build with unittests and final app
# Build with two options:
# No unittests: 
# 1. docker build -t python-app .
# With unittests:
# 2. docker build --build-arg RUN_TESTS=true -t python-app .

# Stage 1: Prepare the environment and install dependencies
FROM python:3.13.0a2-slim-bullseye AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./code /app/code
COPY ./tests /app/tests

# Stage 2: Run the unittests if RUN_TESTS is set to true
FROM python:3.13.0a2-slim-bullseye AS unittest
ARG RUN_TESTS=false
WORKDIR /src
COPY --from=builder /app /src
RUN if [ "$RUN_TESTS" = "true" ] ; then python -m unittest ./tests/app_test.py ; fi

# Stage 3: Run the app and only create an image with the final app
FROM python:3.13.0a2-slim-bullseye AS app
COPY --from=unittest /src/code /app
WORKDIR /app
CMD ["python", "app.py"]

