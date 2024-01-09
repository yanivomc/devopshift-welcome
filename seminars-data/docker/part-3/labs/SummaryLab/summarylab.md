### Lab Intro:
This comprehensive lab covers a wide range of Docker and Docker Compose functionalities, providing a hands-on experience with building,
pushing, and managing multi-container applications. 

The lab is designed to reinforce concepts related to Docker Buildx, Docker Bake, and Docker Compose in a practical, real-world scenario.

### Lab Instructions:

#### Part 1: Creating Flask Applications

1. **Create 3 Flask Applications:**
   - Each application should be in a separate folder: `app1`, `app2`, and `app3`.
   - **server.py (common for all apps):**
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def hello():
         return "This is app X"  # Replace X with 1, 2, or 3 for each app

     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5000)
     ```
   - **requirements.txt (common for all apps):**
     ```
     Flask
     ```
   - Make sure to adjust the message in `server.py` for each app.

#### Part 2: Creating Dockerfiles

1. **Create a Dockerfile for Each Flask App:**
   - The Dockerfile should:
     - Use a suitable base image (e.g., `python:3.8-slim`).
     - Set the working directory.
     - Copy `requirements.txt` and run `pip install`.
     - Copy the `server.py` file.
     - Set the command to run the Flask app (`CMD ["python", "server.py"]`).

#### Part 3: Building and Pushing Images with Buildx

1. **Build and Push Each Image Using Docker Buildx:**
   - Use `docker buildx build` with the `--push` option to build and push each image to your Docker repository.
   - Tag each image appropriately (e.g., `yourrepo/app1:latest`).

#### Part 4: Using Docker Bake with HCL File

1. **Create an HCL File for Docker Bake:**
   - Define build targets for each app with appropriate tags.
   - Create a group that includes all three targets.
   - Use variables for version tagging.
   - Set up dependencies such that `app3` depends on `app2`.

2. **Build and Push Using Docker Bake:**
   - Use `docker buildx bake` with the `--push` option and the HCL file to build and push all apps.

#### Part 5: Docker Compose with .env File

1. **Create a `docker-compose.yml` File:**
   - Define three services, one for each app.
   - Map each app to a different port (`8080`, `8081`, `8082`).
   - Use variables from a `.env` file for image tags.

2. **Create a `.env` File:**
   - Define variables for the image tags of each service (e.g., `APP1_TAG=latest`, `APP2_TAG=latest`, `APP3_TAG=latest`).

#### Instructions for the `.env` File:

- Define variables for the Docker image tags you want to use for each Flask app. For example:
  ```
  APP1_TAG=latest
  APP2_TAG=latest
  APP3_TAG=latest
  ```
- These variables will be used in the `docker-compose.yml` file to specify the version of each app.

#### Instructions for the `docker-compose.yml` File:

- Define a service for each Flask app.
- Use the port mappings `8080`, `8081`, and `8082` for `app1`, `app2`, and `app3`, respectively.
- Use the `.env` file variables for the image tags.

#### Instructions for the Dockerfiles:

- Each Dockerfile should copy the specific app's `server.py` and `requirements.txt`, install dependencies, and set the Flask app as the entry command.

#### Instructions for the HCL File:

- Define a target for each Flask app with its specific context and Dockerfile.
- Use a variable for the tag (version) of each image.
- Create a dependency in the targets where `app3` depends on `app2`.

---

This comprehensive lab covers a wide range of Docker and Docker Compose functionalities, providing a hands-on experience with building, pushing, and managing multi-container applications. The lab is designed to reinforce concepts related to Docker Buildx, Docker Bake, and Docker Compose in a practical, real-world scenario.
