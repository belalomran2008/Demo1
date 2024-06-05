import requests
from bs4 import BeautifulSoup

def convert():
    num = input('       1.Egp --> Usd            2.Usd --> Egp        ')
    if num == '1':
        egp = float(input('How much egp do you want to convert to dollars? '))
        print(egp / b)
    elif num == '2':
        usd = float(input('How much usd do you want to convert to egp? '))
        print(usd * b)

url = requests.get('https://egcurrency.com/en/currency/usd-to-egp/exchange')
soup = BeautifulSoup(url.content, 'html.parser')

prc = soup.find_all('div', attrs = 'd-flex gap-5 row-gap-2 align-items-center flex-wrap mb-2')

a = prc[0].find('b').get_text()

b = float(a)

convert()