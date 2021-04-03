import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="harschdb")

mycursor = mydb.cursor()

mycursor.execute("Select * from employee")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)
