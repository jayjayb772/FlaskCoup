from Subtasks.databaseController import mydb, mycursor
def saveToDB(player, uuid, action, coins, gameCode):
    sql = "INSERT INTO t_events (player, uuid, action, coins, gamecode) VALUES (%s, %s, %s, %s, %s)"
    val = (player, uuid, action, coins, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    #mycursor.fetchall()
    return mydb.cmd_query('SELECT * FROM t_events LIMIT 5;')


#print(saveToDB('Jacob', '4','took three as Duke', 5, 12345))
