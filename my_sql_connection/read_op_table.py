import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="xxx", database="xxx")

mycursor = mydb.cursor()

mycursor.execute("Select * from employee")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)
