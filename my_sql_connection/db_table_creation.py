import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="denka")

mycursor = mydb.cursor()

mycursor.execute("create table TBPARLIAMENTARIANS_SV("
                 "id bigint(50),"
                 "firstName varchar(50),"
                 "lastName varchar(100),"
                 "gender varchar(10),"
                 "dateOfBirth int(12),"
                 "nationalParty varchar(10),"
                 "constituency varchar(50),"
                 "status varchar(50),"
                 "picture varchar(100)"
                 ")")

mydb.commit()

#mycursor.execute("Show tables")

#for tb in mycursor:
#    print(tb)
