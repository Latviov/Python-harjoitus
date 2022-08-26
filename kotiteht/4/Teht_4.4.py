import random
x= random.randint(1, 10)
num=int
while num!=x :
    num = int(input("Arvaa luku: "))
    if num>x :
        print("Luku on pienempi!")
    elif num<x :
        print("Luku on suurempi")
    elif num==x :
        (print(f"Arvasit oikein! Luku oli: {(x)} "))
        break