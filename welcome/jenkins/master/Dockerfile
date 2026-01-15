# Starting off with the Jenkins base Image
# Using Specific version to avoid issues (2.479.3 is up2date to dec 11 2024)
FROM jenkins/jenkins:2.546
 
# Running as root to install system dependencies and have socket access
USER root
RUN apt-get update && apt-get install -y lsb-release curl
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli && rm -rf /var/lib/apt/lists/*

# Installing the plugins we need to the reference directory
# This ensures Jenkins syncs them to /var/jenkins_home/plugins on every boot
RUN /bin/jenkins-plugin-cli --plugin-download-directory /usr/share/jenkins/ref/plugins --plugins \
    git \
    matrix-auth \
    credentials-binding \
    workflow-aggregator \
    docker-workflow \
    blueocean \
    job-dsl \
    workflow-job \
    workflow-cps \
    ws-cleanup \
    http_request \
    configuration-as-code \
    copyartifact \
    throttle-concurrents \
    docker-plugin \
    docker-commons \
    docker-java-api \
    ssh-slaves \
    bouncycastle-api \
    command-launcher \
    structs

# Stay as root to ensure we can read/write the host Docker socket
# USER jenkins (removed to avoid Permission Denied on /var/run/docker.sock)
 
# Setting up environment variables for Jenkins admin user
ENV JENKINS_USER admin
ENV JENKINS_PASS admin
 
# Skip the initial setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false 
 
# Start-up scripts to set number of executors and creating the admin user
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
 
VOLUME /var/jenkins_home
