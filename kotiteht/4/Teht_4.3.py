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
print(f"Pienin luku on: {min(res)} \nSuurin luku on: {max(res)} ")