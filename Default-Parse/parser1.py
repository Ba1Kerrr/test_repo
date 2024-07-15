import requests
from bs4 import BeautifulSoup

def parser(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    parse = soup.findAll('div', class_='styles-list-M1e9B')
    data = []
    for product in parse:
        return page.find('a', class_='product-name').text
        #product_reference = page.find('a', class_='product_reference').text
        #data.append([product_name, product_reference])
#for x in data:
    #print(x)
print(parser("https://www.caprigoshop.ru/72-zakazat-raschet-kukhni-caprigo"))