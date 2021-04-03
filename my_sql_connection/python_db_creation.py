import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)