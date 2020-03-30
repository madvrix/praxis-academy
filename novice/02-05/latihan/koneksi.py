import mysql.connector
db=mysql.connector.Connect(
    host='localhost',
    user='root',
    password=''
)

if db.is_connected():
    print("Database telah terhubung")