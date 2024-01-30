import requests

def fetchAndSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://www.pokemon.com/us/pokedex"

fetchAndSave(url, "data/pokemon.html")