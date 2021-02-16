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
                sh 'C:\Users\ADMIN\AppData\Local\Programs\Python\Python39\python.exe -m py_compile sources/add2vals.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
       
        }
    }
