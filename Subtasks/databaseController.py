from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)
mycursor = mydb.cursor(dictionary=True, buffered=True)