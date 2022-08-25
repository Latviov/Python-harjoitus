kuha= int(input("Anna kuhan pituus: "))
if  kuha < 37 :
    lyhyt = (37 - kuha)
    print(f"heitä vittuu, {lyhyt:0.0f}cm liian pieni")
else:
    print("kuha on vitu fresh")