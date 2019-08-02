from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)


def getPlayers(gameCode):
    cursor = mydb.cursor(dictionary=True)
    sql="SET @gameCode =\""
    sql = sql+gameCode
    sql=sql+"\";"
    print(sql)
    cursor.execute(sql)
    sql = "SELECT * FROM t_players WHERE gameCode = @gameCode;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all

def getEvents():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_events ORDER BY id DESC;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all