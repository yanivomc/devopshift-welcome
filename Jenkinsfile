pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("andreigur5001/registry:build", "-f welcome/Dockerfile .")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.build("andreigur5001/registry:test", "--target test -f welcome/Dockerfile .")
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', '97053140-a004-4ce9-bfef-eabd2e5808c4') {
                        docker.image("andreigur5001/registry:build").push("build")
                        docker.image("andreigur5001/registry:test").push("test")
                    }
                }
            }
        }
    }
}
