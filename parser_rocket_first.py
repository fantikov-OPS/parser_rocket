import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://www.mebelshara.ru/'
URL = 'https://www.mebelshara.ru/contacts'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


html = get_html(url=URL)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='city-item')
    result = []

    for item in items:
        result.append(
            {
                "address": f"{item.find('h4', class_='js-city-name').get_text()},  {item.find('div', class_='shop-list').find('div')['data-shop-address']}",
                "latlon": [float(item.find('div', class_='shop-list').find('div')['data-shop-latitude']),
                           float(item.find('div', class_='shop-list').find('div')['data-shop-longitude'])],
                "name": item.find('div', class_="shop-list").find('div')['data-shop-name'],
                "phones": item.find('div', class_="shop-list").find('div')['data-shop-phone'],
                'working_hours': f"[{item.find('div', class_='shop-list').find('div')['data-shop-mode1']} {item.find('div', class_='shop-list').find('div')['data-shop-mode2']}]"

            }

        )
    return result


def parcer():
    html = get_html(URL)
    if html.status_code == 200:
        result = []
        html = get_html(URL)
        result.extend(get_content(html.text))
        print(result)
        with open('first.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(result, indent=4, ensure_ascii=False))
    else:
        print('Error')


parcer()
