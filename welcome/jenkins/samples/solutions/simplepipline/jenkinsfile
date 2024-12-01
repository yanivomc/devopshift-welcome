pipeline {
    agent any

    environment {
        PYENV_HOME = "${WORKSPACE}/welcome/app/flask-volt-dashboard/.pyenv"
        PROJECT_HOME = "${WORKSPACE}/welcome/app/flask-volt-dashboard"
        FLASK_APP = 'run.py'
        FLASK_ENV = 'development'
    }

    stages {
        stage('Clone Flask Project') {
            steps {
                // Use the Git plugin to clone the repository
                git branch: 'jenkins-workshop', url: 'https://github.com/yanivomc/devopshift-welcome.git'
            }
        }

        stage('Setup Python Environment and Install Dependencies') {
            steps {
                dir("${PROJECT_HOME}") {
                    script {
                        // Install virtualenv if not available
                        sh '''#!/bin/bash
                        if ! command -v virtualenv &> /dev/null; then
                            echo "Installing virtualenv..."
                            pip install virtualenv
                        fi

                        # Delete previously built virtualenv and create a new one
                        rm -rf $PYENV_HOME
                        virtualenv $PYENV_HOME
                        source $PYENV_HOME/bin/activate

                        # Install required Python packages
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Flask Application') {
            steps {
                dir("${PROJECT_HOME}") {
                    script {
                        // Run Flask app within the virtual environment
                        sh '''#!/bin/bash
                        source $PYENV_HOME/bin/activate
                        tasks=$(pgrep -f "flask run")
                        if [ -n "$tasks" ]; then
                            echo "Stopping existing Flask application..."
                            for pid in $tasks; do
                                kill -9 $pid
                                echo "Killed process $pid"
                            done
                        fi

                        echo "Starting Flask application on 0.0.0.0:5005..."
                        nohup flask run --host=0.0.0.0 --port=5005 > flask_app.log 2>&1 &
                        '''
                    }
                }
            }
        }

        stage('Verify Application') {
            steps {
                dir("${PROJECT_HOME}") {
                    script {
                        // Sleep to allow Flask to start
                        sleep 5

                        // Verify Flask application is running
                        def tasks = sh(script: "pgrep -f 'flask run'", returnStatus: true) ? '' : sh(script: "pgrep -f 'flask run'", returnStdout: true).trim()
                        if (!tasks) {
                            // Print error message and show the flask_app.log file content
                            echo "There is a problem with our flask application - printing log below"
                            sh 'cat flask_app.log'
                            error "Flask application is not running!"
                        } else {
                            echo "Flask application is running successfully."
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            dir("${PROJECT_HOME}") {
                echo 'Cleaning up workspace...'
                sh 'rm -rf $PYENV_HOME'
            }
        }
    }
}