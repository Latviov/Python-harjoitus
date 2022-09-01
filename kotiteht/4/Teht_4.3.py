num=int
list=[]
res=[]
while num!="" :
    num= str(input("Anna luku: "))

    if num!="" :
        #num=int
        list.append(num)
        res = [eval(i) for i in list]
    if input == "":
            print(f"Pienin luku on: {min(res)} \nSuurin luku on: {max(res)} ")
            break