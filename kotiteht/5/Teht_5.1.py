import random
x=int(input("Syötä noppien määrä: "))
summa=0

for noppa in range (x):
    noppa = random.randint(1, 6)
    summa += noppa

print(f"Lukema on: {summa}")