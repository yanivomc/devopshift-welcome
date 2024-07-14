FROM  ubuntu:20.04 as builder 
################################################
# Gurdbox setup
################################################
ENV TZ=Asia/Jerusalem
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Make sure the package repository is up to date.
RUN apt-get update && \
    apt-get -qy upgrade && \
    apt-get install -qy git && \
# Install JDK 8 (latest stable edition at 2019-04-01)
    apt-get install -qy openjdk-8-jdk && \
# Autoremove
    apt-get -qy autoremove 
#
RUN apt install iputils-ping  patchelf=0.10-2build1 git  default-jdk=2:1.11-72 plantuml=1:1.2018.13+ds-2 doxygen=1.8.17-0ubuntu2 graphviz=2.42.2-3build2 xsltproc=1.1.34-4 python3-pip=20.0.2-5ubuntu1.6 curl vim cifs-utils=2:6.9-1ubuntu0.1 nfs-common=1:1.3.4-2.5ubuntu3.4 -y

RUN pip3 install requests==2.22.0 && \
    pip3 install Atlassian-python-API && \
    git config --global http.sslVerify false
RUN mkdir -p /home/ciuser/sdk && \
    mkdir -p /home/ciuser/.jfrog && \
    mkdir -p /home/ciuser/.ssh
