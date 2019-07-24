from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)


def saveToDB(player, uuid, action, coins, gameCode):
    mycursor = mydb.cursor()
    sql = "INSERT INTO t_events (player, uuid, action, coins, gamecode) VALUES (%s, %s, %s, %s, %s)"
    val = (player, uuid, action, coins, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.fetchmany(2)


print(saveToDB('Jacob', '4','took three as Duke', 5, 12345))
