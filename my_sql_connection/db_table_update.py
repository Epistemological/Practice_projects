import mysql.connector
from Polbase import sv_parliament

db_connection = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="xxx",
                                       database='xxx')

cursor = db_connection.cursor()


def update_table(data):
    """ Updating mysql database with pandas dataframe """

    cols = "`,`".join([str(i) for i in data.columns.tolist()])

    for i,row in data.iterrows():
        sql = "INSERT INTO tbparliamentarians_sv (`" + cols + "`) VALUES (" + "%s, "*(len(row)-1) + "%s)"
        cursor.execute(sql, tuple(row))

update_table(sv_parliament.swe_parliament())

db_connection.commit()
