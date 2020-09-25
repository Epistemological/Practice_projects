from sqlalchemy import create_engine

import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM Orders ")
df = pd.DataFrame(rs.fetchall())
con.close()

#context manager --> slippa stänga anslutningen senare
with engine.connect() as con:
#hur man tar ut specifika kolumner
rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
df = pd.DataFrame(rs.fetchmany(size=5))
#rättar till kolumner
df.column = rs.keys()

#ta ut ett specifikt bord från databasen (filtering)
"SELECT * FROM Customer WHERE Country = 'Canada'"
#beställa sql query resultat
"SELECT * FROM Customer ORDER BY SupportRepId"

#hämta ut data med än mindre kod, 2 argument
df = pd.read_sql_query("SELECT * FROM Orders", engine)

#kombinera två kolumner från olika bord till ett nytt bord,
# ur vilket man sen hämtar ut de två kolumnerna

with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.column = rs.keys()
    print(df.head())

#i pandas + kondition
df = pd.read_sql_query("SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = ArtistID WHERE Title = 'Andersson'", engine)
print(df.head())
