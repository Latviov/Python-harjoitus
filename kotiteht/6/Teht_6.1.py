import random

def dice_throw():
    noppa = random.randint(1, 6)
    return noppa
while True:
    noppa=dice_throw()
    print(noppa)
    if noppa ==6:
        break