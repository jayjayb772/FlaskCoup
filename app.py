from flask import Flask, render_template, redirect, url_for, request
from Subtasks import savePlayerToDB, saveEventToDB, databaseController
application = Flask(__name__)


@application.route('/')
def mainPage():
    return render_template('mainPage.html')


@application.route('/join')
def login():
    return render_template('joinPage.html')

@application.route('/waitingRoom/<player>')
def waitingRoom(player):
    return 'welcome %s' % player
    # TODO:
    # Render page that will update when a new player is added
    # Shows how many players and how many of each card
    # Highlghts user on page

@application.route('/joinSubmit', methods=['POST'])
def joinSubmit():
    player = request.form['Name']
    gameCode = request.form['GameCode']
    savePlayerToDB.saveToDB(player, gameCode)
    players =databaseController.getPlayers(gameCode)
    saveEventToDB.saveToDB(player,'joined the game', 2, gameCode)
    events = databaseController.getEvents()
    return redirect(url_for('waitingRoom', player=player))
    # TODO:
    # Save things to DB
    # pass game code and returned user ID to page

@application.route('/playing/<player>')
def inGame():
    return



if __name__ == '__main__':
    application.run()
