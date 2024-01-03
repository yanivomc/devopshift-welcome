pipeline {
   agent any
   environment {
       // Environment variables can be defined here
       NODEJS_HOME = tool name: 'nodejs', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
       PATH = "${env.NODEJS_HOME}/bin:${env.PATH}"
   }
   stages {
       stage('Checkout') {
           steps {
               git branch: 'elbit/jenkinsdec26',
                   url: 'https://github.com/yanivomc/devopshift-welcome.git',
                   userRemoteConfigs: [
                       [name: 'DSL User', email: 'jenkins-dsl@domain.com']
                   ]
           }
       }
       stage('Build') {
           steps {
               sh '''
                   echo "Test 1"
                   // Add additional build steps here
               '''
           }
       }
       // Additional stages like 'Test', 'Deploy' etc. can be added here
   }
   triggers {
       pollSCM('H/5 * * * *')
   }
   tools {
       // Specify the NodeJS installation
       nodejs 'nodejs'
   }
   post {
       always {
           echo 'This will always run regardless of the result.'
       }
       success {
           echo 'Pipeline completed successfully.'
       }
       failure {
           echo 'Build failed.'
           // Email notifications or other steps can be added here
       }
   }
}