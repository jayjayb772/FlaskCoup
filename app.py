from flask import Flask, render_template, redirect, url_for, request
from Subtasks import savePlayerToDB
app = Flask(__name__)


@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/join')
def login():
    return render_template('joinPage.html')

@app.route('/waitingRoom/<player>')
def waitingRoom(player):
    return 'welcome %s' % player
    # TODO:
    # Render page that will update when a new player is added
    # Shows how many players and how many of each card
    # Highlghts user on page

@app.route('/joinSubmit', methods=['POST'])
def joinSubmit():
    player = request.form['Name']
    gameCode = request.form['GameCode']
    uniqueUserID = savePlayerToDB.saveToDB(player, gameCode)
    return redirect(url_for('waitingRoom', name=player))
    # TODO:
    # Save things to DB
    # pass game code and returned user ID to page


if __name__ == '__main__':
    app.run(host='0.0.0.0')
