node{
    docker.image('python:3.7.2')
    stage("checkout code"){
        checkout scm
    }
    stage("get requirements"){
        sh "pip install -r requirements.txt"
    }
    stage("build"){
        sh "python app.py &"
    }

}
