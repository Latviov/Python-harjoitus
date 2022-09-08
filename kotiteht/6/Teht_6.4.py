x=[]
def listaus():
    total = 0
    for i in range(0, len(res)):
        total = total + res[i]
    return total
while True:
    num = str(input("Anna luku: "))
    if num =="":
        break
    x.append(num)
    res = [eval(i) for i in x]
    listaus()
print(f"Summa:{(listaus())}")
print(res)