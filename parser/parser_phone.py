import os
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = 'https://www.samsungstore.kg/'
URL = 'https://www.samsungstore.kg/ru/mobilnye_ustroystva/smartfony/smartfons/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 '
}


@csrf_exempt
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-sm-4 col-xs-12')
    phone = []

    for item in items:
        phone.append(
            {
                'title': item.find('div', class_='oneitem').find('h3').get_text(strip=True),
                'price': item.find('div', class_='price').get_text(strip=True),
                'image': HOST + item.find('div', class_='image').find('img').get('src')
            }
        )

    return phone


@csrf_exempt
def parser_func():
    html = get_html(URL)
    if html.status_code == 200:
        smartphone = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            smartphone.extend(get_data(html.text))

        # Downloading images and changing their urls to local path to images
        for i in range(len(smartphone)):
            urlretrieve(smartphone[i]['image'], 'media/smartphone/' + os.path.basename(smartphone[i]['image']))
            smartphone[i]['image'] = 'smartphone/' + os.path.basename(smartphone[i]['image'])

        return smartphone
    else:
        raise ValueError('Something goes wrong with parser function!')
