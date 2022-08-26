tunnus=str
salasana=str
i=int(5)
while i>0 :
    tunnus=(input("Syötä tunnus: "))
    salasana=(input("Syötä salasana: "))
    if tunnus=="python" and salasana=="rules" :
        print("Tervetuloa!")
        break
    i-= 1
if i==0 and tunnus!="python" and salasana!="rules" :
        print("Pääsy evätty!")
