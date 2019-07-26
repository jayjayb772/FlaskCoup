from Subtasks.databaseController import mydb, mycursor
def saveToDB(player, gameCode):
    sql = "INSERT INTO t_players (name, gameCode) VALUES (%s, %s)"
    val = (player, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    #mycursor.fetchall()
    return mycursor.getlastrowid()
