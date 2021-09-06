import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='33066',
    database='admin'
)

print(mydb)

if(mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")