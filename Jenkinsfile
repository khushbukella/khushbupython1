pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'docker pull python'
                bat  'docker build -t khushbupython1 . '
                bat  'docker run -it --rm --name my-running-app khushbupython1'
            }
        }
        }
    }
