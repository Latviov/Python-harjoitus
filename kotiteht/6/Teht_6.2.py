import random
x = int(input("Syötä nopan tahkot: "))
y=0

def dice_throw():
    noppa = random.randint(1, x)
    return noppa
while True:
    noppa=dice_throw()
    print(noppa)
    y+=1
    if noppa ==x:
        print(f"Noppaa heitettiin {y} kertaa")
        break