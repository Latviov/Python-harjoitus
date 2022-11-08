import requests


base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_avain = "3db299e3f46095bd463bc5270384d660"
kaupunki = input("Syötä kaupunki: ")

url = base_url + "appid=" + api_avain + "&q=" + kaupunki + "&units=metric&lang=fi"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        temp = json_response['main']['temp']
        description = json_response['weather'][0]['description']
        country = json_response['sys']['country']
        print(f"{country}\n"
              f"{kaupunki}\n"
              f"Lämpötila: {temp}°C\n"
              f"Sää: {description}")
    if response.status_code == 404:
        print(f"Kaupunkia: {kaupunki}, ei löydy :(")

except requests.exceptions.RequestException as e:
    print("hakua ei voitu suorittaa" + str(e))