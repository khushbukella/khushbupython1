pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                bat 'python --version'
            }
        }
       
        }
    }
