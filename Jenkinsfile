pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.9.1'
                }
            }
            steps {
                bat 'python3 -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        }
    }
