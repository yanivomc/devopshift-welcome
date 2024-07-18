pipeline {
    agent any
    environment {
        IMAGE_NAME = 'my-docker-image'
        VERSION = "v${env.BUILD_NUMBER}"
        REPO = 'andreigur5001/registry'
        CREDENTIALS_ID = '97053140-a004-4ce9-bfef-eabd2e5808c4'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/andreiGur/devopshift-welcome.git', branch: 'jenkins-workshop'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker build --target build --tag ${IMAGE_NAME}:${VERSION}-build -f welcome/app/bookinfo/src/productpage/Dockerfile .'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'docker build --target test --tag ${IMAGE_NAME}:${VERSION}-test -f welcome/app/bookinfo/src/productpage/Dockerfile .'
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
