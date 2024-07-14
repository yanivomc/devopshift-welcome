# Starting off with the Jenkins base Image
# Using Specific version to avoid issues (2.426.3 is up2date to aug jul14 2024)
FROM jenkins/jenkins:2.452.3
 
# Installing the plugins we need using the in-built jenkins-plugin-cli script instead of manual install plugins
RUN /bin/jenkins-plugin-cli --plugins git matrix-auth credentials-binding workflow-aggregator docker-workflow blueocean job-dsl workflow-job workflow-cps 
 
# Setting up environment variables for Jenkins admin user
ENV JENKINS_USER admin
ENV JENKINS_PASS admin
 
# Skip the initial setup wizard
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false -Dhudson.security.csrf.DefaultCrumbIssuer.EXCLUDE_SESSION_ID=true
 
# Start-up scripts to set number of executors and creating the admin user
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/
 
VOLUME /var/jenkins_home
