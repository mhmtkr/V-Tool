import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port='33066',
    database='admin'
)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE")