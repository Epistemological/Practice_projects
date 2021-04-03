import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="xxx", database="xxx")

mycursor = mydb.cursor()

sql = "DELETE FROM employee WHERE name = 'Harshit' "

mycursor.execute(sql)

mydb.commit()
