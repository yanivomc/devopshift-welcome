# Build stage
FROM ubuntu:20.04 as builder

ENV TZ=Asia/Jerusalem
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make sure the package repository is up to date
RUN apt-get update && \
    apt-get -qy upgrade && \
    apt-get install -qy \
    git \
    openjdk-8-jdk \
    iputils-ping \
    patchelf \
    default-jdk \
    plantuml \
    doxygen \
    graphviz \
    xsltproc \
    python3-pip \
    curl \
    vim \
    cifs-utils \
    nfs-common && \
    apt-get -qy autoremove

# Install Python packages
RUN pip3 install requests==2.22.0 Atlassian-python-API && \
    git config --global http.sslVerify false

RUN mkdir -p /home/ciuser/sdk /home/ciuser/.jfrog /home/ciuser/.ssh

# Test stage
FROM builder as test

# Add your test commands here, for example:
# RUN some-test-command

# Final stage
FROM ubuntu:20.04

ENV TZ=Asia/Jerusalem
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy the necessary files from the builder stage
COPY --from=builder /home/ciuser /home/ciuser

CMD ["bash"]
