import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="harschdb")

mycursor = mydb.cursor()

sql = "DELETE FROM employee WHERE name = 'Harshit' "

mycursor.execute(sql)

mydb.commit()
