x=int

def gallona():
    litra=x*3.785
    return litra
while True:
    x = int(input("Negatiivinen luku sulkee softan.\nSyötä gallonat: "))
    litra=gallona()
    if x <0:
        break
    else:
        print(f"{litra:.2f}")