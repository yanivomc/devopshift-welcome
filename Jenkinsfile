{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 pipeline \{\
    environment \{\
        IMAGE_NAME = 'my-docker-image'\
        VERSION = "v$\{env.BUILD_NUMBER\}"\
        REPO = 'my-docker-repo'\
        CREDENTIALS_ID = 'docker-credentials'\
    \}\
    agent any\
    stages \{\
        stage('Checkout') \{\
            steps \{\
                git url: 'https://github.com/username/devopshift-welcome.git', branch: 'jenkins-workshop'\
            \}\
        \}\
        stage('Build') \{\
            steps \{\
                script \{\
                    // Build the Docker image for the build stage\
                    sh 'docker build --target build --tag $\{IMAGE_NAME\}:$\{VERSION\}-build .'\
                \}\
            \}\
        \}\
        stage('Test') \{\
            steps \{\
                script \{\
                    // Build and test the Docker image\
                    sh 'docker build --target test --tag $\{IMAGE_NAME\}:$\{VERSION\}-test .'\
                    sh 'docker run --rm $\{IMAGE_NAME\}:$\{VERSION\}-test'\
                \}\
            \}\
        \}\
        stage('Push') \{\
            steps \{\
                script \{\
                    docker.withRegistry('https://index.docker.io/v1/', "$\{CREDENTIALS_ID\}") \{\
                        sh 'docker push $\{REPO\}/$\{IMAGE_NAME\}:$\{VERSION\}'\
                        sh 'docker tag $\{REPO\}/$\{IMAGE_NAME\}:$\{VERSION\} $\{REPO\}/$\{IMAGE_NAME\}:latest'\
                        sh 'docker push $\{REPO\}/$\{IMAGE_NAME\}:latest'\
                    \}\
                \}\
            \}\
        \}\
    \}\
\}\
}