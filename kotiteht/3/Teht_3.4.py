vuosi= float(input("Anna vuosiluku: "))
if vuosi%4==0 :
    if vuosi%100==0 and vuosi%400==0:
        print("Karkausvuosi!")
    elif vuosi%4==0 and vuosi%100!=0 :
        print("Karkausvuosi")
    elif vuosi%100==0 and vuosi%400!=0 :
        print("Ei karkausvuosi!")
else :
    print("Ei karkausvuosi!")
# vihtu