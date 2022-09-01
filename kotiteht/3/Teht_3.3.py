suku= input("Oletko mies vai nainen: ")
suku=suku.lower()


if suku != "mies" and suku != "nainen" :
    raise SystemExit(print("Koita nyt edes"))
hemo= float(input("Anna hemoglobiiniarvosi: "))
if suku == "mies":
    if hemo >= 134 and hemo <=195:
        print ("Hemoglobiini normaali")
    elif hemo <134:
            print( "Hemoglobiinisi on alhainen")
    elif hemo < 195:
                print ("Hemoglobiinisi on korkealla")
if suku == "nainen":
    if hemo >= 117 and hemo <=175:
        print( "Hemoglobiini normaali")
    elif hemo <117:
            print( "Hemoglobiinisi on alhainen")
    elif hemo < 175:
                print( "Hemoglobiinisi on korkealla")
