import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas
import lxml
from random import choice
from time import sleep

host = 'https://www.mosvideopro.ru'
url = 'https://www.mosvideopro.ru/categories/bezprovodnye-ip-videoregistratory'

DECKTOP_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
NAME_headers = ['link', 'name_prod', 'price']
data = []
def randon_headers():
    return {'User-Agent': choice (DECKTOP_AGENTS), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}



def parser(name_headers):
    r = requests.get ('https://www.mosvideopro.ru/categories/bezprovodnye-ip-videoregistratory', headers = randon_headers())
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')
    items = soup.find_all('div', class_='products-view-block cs-br-1 js-products-view-block')
    for item in items:
        link = item.find('a', class_='products-view-name-link').get('href')
      
        name_prod = item.find('a', class_='products-view-name-link').get_text()
        price = item.find('div', class_='price-number').get_text()
        #picture = item.find('div', class_='products-view-picture-link').get('href')
        sleep(3)
        data.append([link, name_prod, price])
        file = pd.DataFrame(data, columns=name_headers)
        file.to_csv('D:\Games\est.csv', sep=';', encoding='utf8')

parser(NAME_headers)


