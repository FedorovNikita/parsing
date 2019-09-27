import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['url'], data['adress'], data['square'], data['year'], data['floor']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', class_="table-bordered").find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        url = 'http://dom.mingkh.ru' + tds[2].find('a').get('href')
        adress = tds[2].text
        square = tds[3].text
        year = tds[4].text
        floor = tds[5].text

        data = {'url': url, 'adress': adress, 'square': square, 'year': year, 'floor': floor}
        write_csv(data) 

def main():
    pattern = 'http://dom.mingkh.ru/chelyabinskaya-oblast/chelyabinsk/houses?page={}'
    for i in range(0, 2): #71
        url = pattern.format(str(i))
        get_page_data(get_html(url))

if __name__ == '__main__':
    main()