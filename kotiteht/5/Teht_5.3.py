x = int(input("Syötä luku: "))
flag = False

for i in range(2, x) :
    t=x%i
    if t==0 :
        flag = True
        break

if flag:
    print("Luku ei ole alkuluku")
else :
    print("Luku on alkuluku")