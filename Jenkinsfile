pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
        bat 'docker'
        bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
       
        }
    }
