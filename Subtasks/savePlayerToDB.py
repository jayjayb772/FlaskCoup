from Subtasks.databaseController import mydb
def saveToDB(player, gameCode):
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_players (name, gameCode) VALUES (%s, %s)"
    val = (player, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    return