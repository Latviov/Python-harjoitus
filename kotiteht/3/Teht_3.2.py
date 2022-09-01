hytti= (input("Mikä on hyttiluokkasi: "))
hytti=hytti.lower()
if hytti == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "a":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "b":
            print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else :
                    print("Virheellinen hyttiluokka.")