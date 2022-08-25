#x, y, z = [int(x) for x in input("Enter three values: ").split()]
s,r,t= [int(x) for x in input("Anna kolme kokonaislukua:").split()]
summa=s+r+t
tulo=s*r*t
keski=(s+r+t)/3
print(f"Lukujen summa on: ",summa)
print(f"Lukujen tulo on: ",tulo)
print(f"Lukujen keskiarvo on: ",keski)