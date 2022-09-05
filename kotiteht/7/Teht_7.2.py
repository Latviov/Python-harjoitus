x=str
nimet=set()
while x!="":
    x=input("Anna nimi: ")
    x=x.lower()
    if x not in nimet and x!="":
        print("Uusi nimi!")
        nimet.add(x)
    elif x in nimet:
        print("Aiemmin syötetty nimi!")
    if x=="":
        print(x)
        break
print(nimet)