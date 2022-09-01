import random
o=[]
i=0
n=10
def remove_odd_elements():
    for x in range(n):
        o.append(random.randint(1, 100))
    print(o)
    for i in o[:]:
        if i%2!=0:
            o.remove(i)
    return o
print(remove_odd_elements())