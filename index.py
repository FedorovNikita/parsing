import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_column_name():
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        col1 = 'Адрес'
        col2 = "Год ввода в эксплуатацию"
        col3 = "Детская площадка"
        col4 = "Дом признан аварийным"
        col5 = "Дополнительная информация"
        col6 = "Количество жилых помещений"
        col7 = "Класс энергетической эффективности"
        col8 = "Количество лифтов"
        col9 = "Количество подъездов"
        col10 = "Лифты"
        col11 = "Наибольшее количество этажей"
        col12 = "Наименьшее количество этажей"
        col13 = "Количество нежилых помещений"
        col14 = "Площадь жилых помещений м2"
        col15 = "Площадь нежилых помещений м2"
        col16 = "Площадь помещений общего имущества м2"
        col17 = "Площадь зем. участка общего имущества м2"
        col18 = "Площадь парковки м2"
        col19 = "Серия, тип постройки здания"
        col20 = "Спортивная площадка"
        col21 = "Формирование фонда кап. ремонта"
        col22 = "Тип дома"



        writer.writerow((col1,
                        col2,
                        col3,
                        col4,
                        col5,
                        col6,
                        col7,
                        col8,
                        col9,
                        col10,
                        col11,
                        col12,
                        col13,
                        col14,
                        col15,
                        col16,
                        col17,
                        col18,
                        col19,
                        col20,
                        col21,
                        col22))
                        
def write_csv(data):
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['address'],
                        data['year'],
                        data['child_yard'],
                        data['emergency_house'],
                        data['more_info'],
                        data['number_apartments'],
                        data['energy_class'],
                        data['number_elevators'],
                        data['number_entrances'],
                        data['elevators'],
                        data['max_floor'],
                        data['min_floor'],
                        data['number_apartments_without_people'],
                        data['square_number_apartments'],
                        data['square_number_apartments_without_people'],
                        data['square_common_property'],
                        data['land_square_common_property'],
                        data['square_parking'],
                        data['series_type_construction'],
                        data['sports_ground'],
                        data['formation_capital_repair'],
                        data['type_building']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ad = soup.find('ul', class_='breadcrumb').find_all('li')[-1].find('a').text.split(',')
    address = ''.join(ad)
    # НЕЗАБУДЬ ПОСТАВИТЬ ВСЕ ПЕРЕМЕННЫЕ
    year = '-'
    child_yard = '-'
    emergency_house = '-'
    more_info = '-'
    number_apartments = '-'
    energy_class = '-'
    number_elevators = '-'
    number_entrances = '-'
    elevators = '-'
    max_floor = '-'
    min_floor = '-'
    number_apartments_without_people = '-'
    square_number_apartments = '-'
    square_number_apartments_without_people = '-'
    square_common_property = '-'
    land_square_common_property = '-'
    square_parking = '-'
    series_type_construction = '-'
    sports_ground = '-'
    formation_capital_repair = '-'
    type_building = '-'

    trs = soup.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        i = 0
        while i < len(tds):
            if (tds[i].text == 'Год ввода в эксплуатацию'):
                year = tds[-1].text

            if (tds[i].text == 'Детская площадка'):
                child_yard = tds[-1].text
            
            if (tds[i].text == 'Дом признан аварийным'):
                emergency_house = tds[-1].text
            
            if (tds[i].text == 'Дополнительная информация'):
                more_info = tds[-1].text
            
            if (tds[i].text == 'Количество жилых помещений'):
                number_apartments = tds[-1].text

            if (tds[i].text == 'Класс энергетической эффективности'):
                energy_class = tds[-1].text

            if (tds[i].text == 'Количество лифтов'):
                number_elevators = tds[-1].text

            if (tds[i].text == 'Количество подъездов'):
                number_entrances = tds[-1].text

            if (tds[i].text == 'Лифты'):
                elevators = tds[-1].text

            if (tds[i].text == 'Наибольшее количество этажей'):
                max_floor = tds[-1].text
            
            if (tds[i].text == 'Наименьшее количество этажей'):
                min_floor = tds[-1].text
            
            if (tds[i].text == 'Количество нежилых помещений'):
                number_apartments_without_people = tds[-1].text

            if (tds[i].text == 'Площадь жилых помещений м2'):
                square_number_apartments = tds[-1].text

            if (tds[i].text == 'Площадь нежилых помещений м2'):
                square_number_apartments_without_people = tds[-1].text
            
            if (tds[i].text == 'Площадь помещений общего имущества м2'):
                square_common_property = tds[-1].text

            if (tds[i].text == 'Площадь зем. участка общего имущества м2'):
                land_square_common_property = tds[-1].text
            
            if (tds[i].text == 'Площадь парковки м2'):
                square_parking = tds[-1].text
            
            if (tds[i].text == 'Серия, тип постройки здания'):
                series_type_construction = tds[-1].text
            
            if (tds[i].text == 'Спортивная площадка'):
                sports_ground = tds[-1].text
            
            if (tds[i].text == 'Формирование фонда кап. ремонта'):
                formation_capital_repair = tds[-1].text
            
            if (tds[i].text == 'Тип дома'):
                type_building = tds[-1].text
            i = i + 1

    data = {'address': address, 
            'year': year,
            'child_yard': child_yard,
            'emergency_house': emergency_house,
            'more_info': more_info,
            'number_apartments': number_apartments,
            'energy_class': energy_class,
            'number_elevators': number_elevators,
            'number_entrances': number_entrances,
            'elevators': elevators,
            'max_floor': max_floor,
            'min_floor': min_floor,
            'number_apartments_without_people': number_apartments_without_people,
            'square_number_apartments': square_number_apartments,
            'square_number_apartments_without_people': square_number_apartments_without_people,
            'square_common_property': square_common_property,
            'land_square_common_property': land_square_common_property,
            'square_parking': square_parking,
            'series_type_construction': series_type_construction,
            'sports_ground': sports_ground,
            'formation_capital_repair': formation_capital_repair,
            'type_building': type_building}
    write_csv(data) 
        
def main():
    # url = 'http://dom.mingkh.ru/chelyabinskaya-oblast/chelyabinsk/538552'
    url = 'http://dom.mingkh.ru/chelyabinskaya-oblast/chelyabinsk/535117'
    get_column_name()
    get_page_data(get_html(url))

if __name__ == '__main__':
    main()