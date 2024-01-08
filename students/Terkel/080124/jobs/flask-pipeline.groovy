pipeline {
    agent any // Run on any available agent
    stages {
        stage('Clone') {
            steps {
                git branch: 'elbit/jenkinsdec26', url: 'https://github.com/yanivomc/devopshift-welcome.git'
            }
        }

        stage('Requirments') {
            steps {
                sh 'cat students/Terkel/080124/python-flask/requirements.txt' 
                sh 'pip --version' 
                sh 'pip install -r students/Terkel/080124/python-flask/requirements.txt' 
                catchError(buildResult: 'SUCCESS', message: 'python error', stageResult: 'UNSTABLE') {
                    sh 'python --version' // some block
                }
            }
        }

        stage('Parallel Tests') {
            parallel {
                stage('Unit test') {
                    steps {
                        sh 'echo “unit test”'
                    }
                }
                stage('ntegration test') {
                    steps {
                        sh 'echo “unit test”' 
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline completed success.'
        }
        failure {
            mail bcc: '', body: 'my pipe done fail', cc: '', from: '', replyTo: '', subject: 'my pipe', to: 'terkmail@gmail.com'
        }
    }
}