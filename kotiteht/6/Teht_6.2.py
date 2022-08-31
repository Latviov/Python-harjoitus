import random
x = int(input("Syötä nopan tahkot: "))

def dice_throw():
    noppa = random.randint(1, x)
    return noppa
while True:
    noppa=dice_throw()
    print(noppa)
    if noppa ==x:
        break