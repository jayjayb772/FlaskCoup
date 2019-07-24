from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)


def saveToDB(player, gameCode):
    mycursor = mydb.cursor()
    sql = "INSERT INTO t_players (name, gameCode) VALUES (%s, %s)"
    val = (player, gameCode)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.getlastrowid()
