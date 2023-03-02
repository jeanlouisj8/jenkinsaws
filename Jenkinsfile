pipeline {
    agent any
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }    

        stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jeanlouisj8/jenkinsaws.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest unit_tests.py'
            }
        }
            }
        }

