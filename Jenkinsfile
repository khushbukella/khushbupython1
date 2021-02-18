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
                bat 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage('Submit Stack') {
            steps {
            bat "aws cloudformation create-stack --stack-name khushbustackforcicdd --template-body file://cicd1.json --region 'us-east-1'"
              }
             }
        }
    }
