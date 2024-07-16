pipeline {
    environment {
        IMAGE_NAME = 'my-docker-image'
        VERSION = "v${env.BUILD_NUMBER}"
        REPO = 'my-docker-repo'
        CREDENTIALS_ID = 'docker-credentials'
    }
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/andreiGur/devopshift-welcome.git', branch: 'jenkins-workshop'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Build the Docker image for the build stage
                    sh 'docker build --target build --tag ${IMAGE_NAME}:${VERSION}-build .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Build and test the Docker image
                    sh 'docker build --target test --tag ${IMAGE_NAME}:${VERSION}-test .'
                    sh 'docker run --rm ${IMAGE_NAME}:${VERSION}-test'
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${CREDENTIALS_ID}") {
                        sh 'docker push ${REPO}/${IMAGE_NAME}:${VERSION}'
                        sh 'docker tag ${REPO}/${IMAGE_NAME}:${VERSION} ${REPO}/${IMAGE_NAME}:latest'
                        sh 'docker push ${REPO}/${IMAGE_NAME}:latest'
                    }
                }
            }
        }
    }
}
