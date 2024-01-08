pipeline {
    agent any // Run on any available agent
    stages {
        stage('Clone') {
            steps {
                git branch: 'elbit/jenkinsdec26', url: ''https://github.com/yanivomc/devopshift-welcome.git''
            }
        }

        stage('pip') {
            steps {
                sh 'echo pip install' 
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