pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'docker pull python'
                bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        }
    }
