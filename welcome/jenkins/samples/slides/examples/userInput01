pipeline {
    agent any

    stages {
        stage('Run Application') {
            steps {
                echo 'Starting Flask application...'
            }
        }

        stage('Wait for User Approval') {
            steps {
                script {
                    // Wait for user interaction and store the result
                    def userInput = input message: 'Is the application running successfully?',
                                         parameters: [choice(name: 'Proceed', choices: 'Proceed\nAbort', description: 'Choose an option')]
                    // Set a variable based on user input
                    env.USER_CHOICE = userInput
                }
            }
        }

        stage('Continue the pipeline') {
            // Run this stage ONLY! if the user chooses 'Proceed'

            when {
                expression { env.USER_CHOICE == 'Proceed' }
            }
            steps {
                script {
                    echo 'Continuing the pipeline...'
                }
            }
        }

        stage('Abort the Pipeline') {
            // Run this stage ONLY! if the user chooses 'Abort'
            when {
                expression { env.USER_CHOICE == 'Abort' }
            }
            steps {
                script {
                    error 'Pipeline aborted by the user'
                }
            }
        }

        // Run this stage regardless of the user choice but we will check the user choice in the stage and print a message
        stage('Finalize the Pipeline') {
            steps {
                script {
                    if (env.USER_CHOICE == 'Proceed') {
                        echo 'Pipeline completed successfully'
                    } else {
                        echo 'Pipeline aborted by the user'
                    }
                }
            }
        }
    }
}