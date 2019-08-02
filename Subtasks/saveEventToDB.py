from Subtasks.databaseController import mydb
def saveToDB(player, action, coins, gameCode):
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_events (player, action, coins, gamecode) VALUES (%s, %s, %s, %s)"
    val = (player, action, coins, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    return

#print(saveToDB('Jacob', '4','took three as Duke', 5, 12345))
