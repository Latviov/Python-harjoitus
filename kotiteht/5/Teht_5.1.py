import random
x=int(input("Syötä noppien määrä: "))

for noppa in range (x):
    noppa = random.randint(1, 6)
    if x==0 :
        break
    print(f"Lukema on: {noppa}")