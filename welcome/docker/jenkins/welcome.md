🅓🅔🅥🅞🅟🅢🅗🅘🅕🅣

### JENKINS PLAYGROUND
Welcome to Jenkins playground.

Once your terminal is available,
Allow a few moments for your jenkins environments to bootstrap.

**You can follow the status of the process by running:**

    tail -f /var/log/user-data.log

  **Once you see output similar to the following:**
  

> Container jenkins  Starting\
> Container jenkins  Started\
> Container docker-cicd-jenkins-slave-1  Starting\
> Container docker-cicd-jenkins-slave-1  Started\

**You may break the tail command and validate all services are running by executing:**

    cd /home/ubuntu/workarea/docker-cicd
    docker compose  -f docker-compose-jenkins.yml ps --services --status running | awk '{ print "Service:", $1, "is running" }'
    docker compose  -f docker-compose-jenkins.yml ps --services --status exited | awk '{ print "Service:", $1, "exit" }'

Validate that all containers are up and no exited services.

> Service: jenkins-slave is running \
Service: jenkins is running 

**To restart** Jenkins services you may run:

    docker compose -f docker-compose-jenkins.yml restart
---

### Accessing Jenkins
Once all services are up,
you may access **JENKINS UI** by running the following:

**Option 1:** Run the following command in your Terminal:

    echo "Your JENKINS URL is: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):8080"

---

    Username: admin 
    Password:  admin

