from geopy.distance import geodesic
import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='viiskytkuus',
         autocommit=True
         )

def hae(lentoasema):
    sql = "select latitude_deg, longitude_deg from airport where ident = '" + lentoasema + "';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

x=input("Anna ensimmäinen ICAO-koodi: ")
x=x.upper()
hae(x)
y=input("Anna toinen ICAO-koodi: ")
y=y.upper()
hae(y)
print(f"{geodesic(hae(x),hae(y)).km:0.2f} kilometriä välimatkaa")