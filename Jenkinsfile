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
    }
    stage("wsgi?"){
    sh "pip install gunicorn"
    sh "cat app.py
    sh "def app(environ, start_response):
        data = b"Hello, World!\n" start_response("200 OK", [ ("Content-Type", "text/plain"), ("Content-Length", str(len(data))) ])
        return iter([data])""
    sh "gunicorn -w 4 myapp:app"
    }

}