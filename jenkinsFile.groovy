pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('run') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
post {
    always {
        echo 'ok,'
    }
    success {
        echo 'How?'
    }
    failure {
        echo 'Fair.'
    }
}post {
    always{
        echo 'ok,'
    }
    
    success{
        echo 'How?'
    }
    
    always{
        echo 'Fair.'
    }
}
