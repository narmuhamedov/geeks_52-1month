import requests
from bs4 import BeautifulSoup as BS

#ссылка для сайта которую мы парсим
URL = 'https://kinovibe.co/'

#HEADERS - внутрении данные сайта указываем для того что мы не являемся роботом
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

#1 Создание запроса
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 Получение данных через html страницу (консоль разработчика)
def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all("div", class_='custom1-item')
    rezka_list = []

    for item in items:
        title = item.find("div", class_='custom1-title')
        rezka_list.append({
            'title': title,
        })
    return rezka_list

#3 функционал парсинга объединненые 2 функции
def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list_2 = []
        for page in range(1, 2):
            response = get_html('https://kinovibe.co/genreserial/boevik/', params={'page':page})
            rezka_list_2.extend(get_data(response.text))
        return rezka_list_2
    else:
        raise Exception('error in parse')

if __name__ == '__main__':
    print(parsing_rezka())