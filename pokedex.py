import requests
from bs4 import BeautifulSoup

# def fetchAndSave(url, path):
#     r = requests.get(url)
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(r.text)

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

mw_parser_output_div = soup.find('div', class_='mw-parser-output')


# number_cells = soup.find_all('td', style='font-family:monospace,monospace')
# for number_cell in number_cells:
#     number = number_cell.get_text(strip=True)
with open("data/pokemonNumbers.html", "w", encoding="utf-8") as f:
    f.write(mw_parser_output_div.text + '\n')
# print(soup.prettify)
# fetchAndSave(url, "data/pokemon.html")