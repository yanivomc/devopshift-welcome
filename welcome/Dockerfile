# Build stage
FROM ubuntu:20.04 as builder

ENV TZ=Asia/Jerusalem
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make sure the package repository is up to date
RUN apt-get update && \
    apt-get -qy upgrade && \
    apt-get install -qy git && \
    apt-get install -qy openjdk-8-jdk && \
    apt-get -qy autoremove

RUN apt install -y iputils-ping patchelf=0.10-2build1 git default-jdk=2:1.11-72 \
    plantuml=1:1.2018.13+ds-2 doxygen=1.8.17-0ubuntu2 graphviz=2.42.2-3build2 \
    xsltproc=1.1.34-4 python3-pip=20.0.2-5ubuntu1.6 curl vim cifs-utils=2:6.9-1ubuntu0.1 \
    nfs-common=1:1.3.4-2.5ubuntu3.4

RUN pip3 install requests==2.22.0 && \
    pip3 install Atlassian-python-API && \
    git config --global http.sslVerify false

RUN mkdir -p /home/ciuser/sdk && \
    mkdir -p /home/ciuser/.jfrog && \
    mkdir -p /home/ciuser/.ssh

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
