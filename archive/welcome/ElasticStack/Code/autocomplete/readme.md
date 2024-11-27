
# Introduction to the Flask Autocomplete App with Elasticsearch

  

**Content:**

- Brief overview of what the Flask app does.

- Role of Elasticsearch in the app.

- Importance of Docker in ensuring a consistent runtime environment.

  

**Application File Structure**

  

-  **server.py**: Main Flask application logic.

-  **Dockerfile**: Configuration to containerize the Flask app.

-  **templates/**: Folder containing HTML templates.

  
---

**Key Components of server.py**

- Flask as the web framework.

- Elasticsearch client for connecting to and querying ES.

- App routing logic for the search feature.

---
  

**Dockerizing the Flask App**

  
**Why Docker?**

- Ensures consistent environment.

- Simplifies deployment process.

-  `Dockerfile` breakdown:

- Base image: Python 3.9 slim.

- Requirements installation: Flask & Elasticsearch.

- Command to run the app.

  

### Remember to adjust `ES_HOST` in `server.py` if Elasticsearch location changes.

  

**Building and Running the Docker Container**

1. Navigate to the app directory:

~~~
cd /home/ubuntu/workarea/devopshift/welcome/ElasticStack/Code/autocomplete
~~~  

**Build the Docker image:**

~~~
docker build -t flask-es-app .
~~~
  

**Run the Docker container**

~~~
docker run -p 5200:5200 flask-es-app
~~~
  

**Access the Flask app:**
~~~
Open a browser and navigate to http://<your-server-ip>:5200
~~~