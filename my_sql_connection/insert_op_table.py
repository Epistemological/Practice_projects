import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="harschdb")

mycursor = mydb.cursor()

sqlform = "Insert into employee(name, sal) values(%s, %s)"

employees = [("Harshit", 20000), ("amit", 30000), ("ankita", 40000), ]

mycursor.executemany(sqlform, employees)

mydb.commit()