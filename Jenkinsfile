pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'docker pull python'
                bat  'docker build -t khushbupython1 . '
                bat  'winpty docker run -it --rm --name my-running-app khushbupython1'
            }
        }
        }
    }
