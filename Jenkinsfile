pipeline {
    agent any
    stages {
        stage('Build') {
            steps { bat 'python -m py_compile sources/add2vals.py sources/calc.py'}
        }
       stage('test') {
            agent {docker {image 'python:3.9.1'}}
            steps {
                bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
       
        }
    }
