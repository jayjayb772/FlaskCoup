from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)


def saveToDB(player, uuid, action, coins):
    mycursor = mydb.cursor()
    sql = "INSERT INTO t_events (player, uuid, action, coins) VALUES (%s, %s, %s, %d)"
    val = (player, uuid, action, coins)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.fetchmany(5)
