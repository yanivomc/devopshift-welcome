pipeline {
    agent any // Run on any available agent
    stages {
        stage('Clone') {
            steps {
                git {
                remote { url('https://github.com/yanivomc/devopshift-welcome.git') }
                branches('elbit/jenkinsdec26') // this is fine
                }
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