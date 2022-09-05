len={"EFHK":"Helsinki-Vantaan lentoasema",
     "EFTU":"Turun lentoasema",
     "EFVA":"Vaasan lentoasema",
     "EFOU":"Oulun lentoasema"}
x=1
while x<3:
    x=int(input("1/Syötä uusi lentoasema, 2/Hae lentoasemaa, 3/Lopeta:"))
    if x==1:
        n=input("Syötä lentoaseman nimi: ")
        m = input("Syötä lentoaseman ICAO-koodi: ")
        m=m.upper()
        len[m]=n
    elif x==2:
        k=input("Anna lentoaseman ICAO koodi:")
        k=k.upper()
        if k in len:
            print(f"ICAO-koodin {k} Lentoaseman nimi on {len[k]}.")
        elif k not in len:
            print("Virheellinen ICAO")
print("Lopetus!")