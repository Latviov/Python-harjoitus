import random
o=[]
def remove_odd_elements():
    for x in range(10):
        o.append(random.randint(1, 100))
    print(o)
    for i in o[:]:
        if i%2!=0:
            o.remove(i)
    return o
print(remove_odd_elements())