pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'docker pull python'
                bat  'docker build -t khushbupython1 . '
                bat  'docker run --rm --name my-running-app khushbupython1'
            }
        }
        stage('Submit Stack') {
            
            steps {
                withAWS(credentials:'jenkins'){
            bat "aws cloudformation create-stack --stack-name khushbustackforcicdd --template-body file://cicd1.json --capabilities CAPABILITY_NAMED_IAM"}
              }
            
             }
        }
    }
