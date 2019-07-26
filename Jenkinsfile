node{
    docker.image('python:3.7.2')
    stage("checkout code"){
        git 'https://github.com/jayjayb772/FlaskCoup.git'
    }
    stage("get requirements"){
        sh "pip install -r requirements.txt"
    }
    stage("build"){
        sh "gunicorn wsgi:application"
    }

}
