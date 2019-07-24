node{
    docker.image('python:3.7.2')
    stage("checkout code"){
        git 'https://github.com/jayjayb772/FlaskCoup.git'
    }
    stage("get requirements"){
        sh "pip3 install -r requirements.txt"
    }
    stage("build"){
        sh "export FLASK_APP=app.py"
        sh "flaks run"
    }

}