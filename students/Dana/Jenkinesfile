pipeline {
    agent any // Run on any available agent

    stages {
        stage('Clone repository') {
            steps {
                git branch:'elbit/jenkinsdec26' , git: 'https://github.com/yanivomc/devopshift-welcome.git' // Replace with your repository URL
            }
        }

        stage('Build') {
            steps {
                echo “javac”
            }
        }

        stage('Unit Tests') {
            steps {
                echo “unit test”
            }
        }

        stage('Parallel Mock Tests') {
            parallel {
                stage('intergation') {
                    steps {
                        echo “unit test”
                    }
                }
                stage('Mock Test 2') {
                    steps {
                        sh 'echo "Running Mock Test 2"' // Replace with actual test command
                        // Add commands to execute Mock Test 2
                    }
                }
                stage('Allowed to Fail Test') {
                    steps {
                        script {
                            try {
                                sh 'echo "Running test that is allowed to fail"; exit 1' // This test fails
                            } catch (Exception e) {
                                echo "Test failed, but pipeline continues."
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'This will always run regardless of the result.'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}