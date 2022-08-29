num=int
list=[]
while num!="" :
    num= str(input("Anna luku: "))

    if num!="" :
        #num=int
        list.append(num)
        res = [eval(i) for i in list]
    if input == "":
            break
res.sort(reverse=True)
fi = res[0:5]
print(f"Suurin luku on: {(fi)} ")