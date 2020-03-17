import mysql.connector
db=mysql.connector.connect(
    user='root',
    passwd='password',
    host='localhost'
)

if db.is_connected():
    print("Database telah terhubung")