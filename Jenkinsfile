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
                bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
       
        }
    }
