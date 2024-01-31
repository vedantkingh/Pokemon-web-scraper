import requests
from bs4 import BeautifulSoup, UnicodeDammit


def fillTypes(section, forms):
    types = []
    if(len(forms) > 1):
        for form in forms:
            form_section = section.find_all("small", string=form)
            # for abc in form_section:
            #     print(abc.prettify())
            # print(form_section[0].parent.prettify())
            if form_section:
                single_forms = []
                # print(form_section[0].parent.prettify())
                form_types = form_section[0].parent.find_all('b')
                for single_form in form_types:
                    single_forms.append(single_form.text)
                types.append(single_forms)
    else:
        for td in section.find_all('td', style='display: none;'):
            td.extract()
        form_section = section.find_all('b')
        for iter in form_section:
            parent_a = iter.find_parent('a')
            if parent_a and parent_a.has_attr('class'):
                continue
            types.append(iter.text)
        types.pop(0)
    print(types)

def makeFormStats(poke_card, forms):
    type_section = poke_card.find_all('tr')[9]
    fillTypes(type_section, forms)

def saveData(id, name, number_of_forms, forms, form_stats):
    pokemon = {
        "id" : id,
        "name" : name,
        "number_of_forms" : number_of_forms,
        "forms" : forms,
        "form_stats" : form_stats
    }
    return pokemon


url = "https://bulbapedia.bulbagarden.net/wiki/Rotom_(Pok%C3%A9mon)"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

mw_parser_output_div = soup.find('div', class_='mw-parser-output')

tables = mw_parser_output_div.find_all('table')
poke_card = tables[4]

id = poke_card.find('th', class_='roundy', style='background:#FFF;', width='25%').text.replace('\n', '')
name = poke_card.find('big').text.replace('\n', '')


image_section = poke_card.find_all('tr')[3]
form_rows = [tr for tr in image_section.find_all('tr') if not tr.has_attr('style') or 'display:none' not in tr['style']]

with open("data/pokemonNumbers1.html", "w", encoding="utf-8") as f:
    f.write(poke_card.find_all('tr')[8].prettify() + '\n')
forms = []

with open("data/pokemonNumbers2.html", "a", encoding="utf-8") as f:
    for form in form_rows[:-1]:
        for a_tag in form.find_all('a'):
            f.write(a_tag.get('title','') + '\n')
            forms.append(a_tag.get('title',''))

number_of_forms = len(forms)
print(id)
print(name)
print(forms)
print(number_of_forms)
# makeFormStats(poke_card, forms)
print(fillTypes(poke_card.find_all('tr')[8], forms))