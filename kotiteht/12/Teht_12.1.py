import requests


req = "https://api.chucknorris.io/jokes/random"

joke = requests.get(req).json()

print(joke["value"])
