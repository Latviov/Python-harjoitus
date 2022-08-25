import math
le= float(input("Anna leiviskät: "))
nau= float(input("Anna naulat: "))
luo= float(input("Anna luodit: "))
p=nau*32
o=p+luo
t=o*13.3
na=le*20
lu=na*32
g=lu*13.3
h=t+g
kg=h/1000
#kg=le*8.5
loput= h-math.floor(kg)*1000
#math.floor(kg)
print(f"Massa nykyarvoilla: {math.floor(kg)},{loput:0.2f}")