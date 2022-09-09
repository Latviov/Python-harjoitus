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
    sql = "select name, municipality from airport where gps_code= '\"" + lentoasema + "\"';"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)


x= input("Anna ICAO koodi: ")
x=x.upper()
hae(x)