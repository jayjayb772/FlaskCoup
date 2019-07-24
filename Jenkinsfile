node{
    docker.image('python:3.7.2')
    stage("checkout code"){
        git 'https://github.com/jayjayb772/FlaskCoup.git'
    }
    stage("get requirements"){
        sh "sudo pip3 install -r requirements.txt"
    }
    stage("build"){
        sh "sudo export FLASK_APP=app.py"
        sh "sudo python3 app.py >> log.txt 2>&1 &"
    }

}