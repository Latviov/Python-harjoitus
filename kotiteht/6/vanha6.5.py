#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
x=[]
i=0
def remove_odd_elements():
    for i in res[:]:
        if i%2!=0:
            res.remove(i)
    return res
while True:
    num = str(input("Anna luku: "))
    if num =="":
        l = [eval(i) for i in x]
        print(l)
        break
    x.append(num)
    res = [eval(i) for i in x]
    remove_odd_elements()
print(remove_odd_elements())