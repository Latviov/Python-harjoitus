import math
def value():
    p=hal/2
    pa=math.pi*p**2
    v=pa/hinta

    p1=hal1/2
    pa1=math.pi*p1**2
    v1=pa1/hinta1
    if v<v1:
        b="Ensimmäinen pitsa on wörtimpi!"
        return b
    elif v>v1:
        er="Toinen pitsa on wörtimpi!"
        return er

    elif v==v1:
        tr="Iha yhtä wörth"
        return tr

hal = int(input("Anna ensimmäisen pitsan halkaisija: "))
hinta = int(input("Anna ensimmäisen pitsan hinta: "))
hal1 = int(input("Anna toisen pitsan halkaisija: "))
hinta1 = int(input("Anna toisen pitsan hinta: "))
value()
print(f"{value()}")