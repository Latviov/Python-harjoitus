import main
import os

# tää on täällä
x = 0
print("haloo")

def Bush_did_911():
    print("Helppo kiva")


while True:
    flight_number = str(input("Anna lennon numero: ")).upper()

    if flight_number == "AA11":
        os.system('cls')
        main.torni_kaatuu()
        print("Rip pohjoistorni")
        main.time.sleep(2)
        os.system('cls')

    elif flight_number == "UA175":
        os.system('cls')
        main.torni_kaatuu()
        print("Rip etelätorni")
        main.time.sleep(2)
        os.system('cls')

    elif flight_number == "666":
        os.system('cls')
        print("Program Exit")
        break