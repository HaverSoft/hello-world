import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages, basic_url, list_url):
    page = 2
    while page <= max_pages:
        url = list_url + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.findAll('a', {'class': 'subcategory-name'}):
            title = link.string
            href = link.get('href')
            print(title)
            print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


trade_spider(max_pages=3, basic_url='http://www.gombolda.hu',
             list_url='http://www.gombolda.hu/gombok-83?page=')
