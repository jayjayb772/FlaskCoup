from flask import Flask, render_template, redirect, url_for, request, jsonify, json
from Subtasks import savePlayerToDB, saveEventToDB, databaseController
application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def mainPage():
    return Flask.response_class(status=201)
#
#
# @application.route('/join')
# def login():
#     return render_template('joinPage.html')
#
# @application.route('/waitingRoom/<player>')
# def waitingRoom(player):
#     return 'welcome %s' % player
#     # TODO:
#     # Render page that will update when a new player is added
#     # Shows how many players and how many of each card
#     # Highlghts user on page

#
# @application.route('/joinSubmit', methods=['POST'])
# def joinSubmit():
#     print(request)
#     player = request.form['name']
#     gameCode = request.form['gamecode']
#     savePlayerToDB.saveToDB(player, gameCode)
#     players =databaseController.getPlayers(gameCode)
#     saveEventToDB.saveToDB(player,'joined the game', 2, gameCode)
#     events = databaseController.getEvents()
#     return Flask.response_class()


@application.route('/joinSubmit', methods=['POST', 'OPTIONS'])
def joinSubmit():
    data = request.get_json(force=True)
    print(data)
    player = data['name']
    gameCode = data['gamecode']
    savePlayerToDB.saveToDB(player, gameCode)
    players =databaseController.getPlayers(gameCode)
    saveEventToDB.saveToDB(player,'joined the game', 2, gameCode)
    events = databaseController.getEvents()
    return Flask.response_class(status=201)
    # TODO:
    # Save things to DB
    # pass game code and returned user ID to page


@application.route('/getPlayers', methods=['GET'])
def getPlayersInGame():
    return Flask.response_class(status=201)

#get events
@application.route('/getEvents')#, methods=['GET'])
def getEvents():
    return Flask.response_class(response=json.dumps(databaseController.getEvents()), mimetype='application/json')

#take action (player,gamecode,action)

#submit callout orpass

if __name__ == '__main__':
    application.run()
