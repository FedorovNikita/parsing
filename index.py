import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def filter_number(num):
    number = num.split(' ')
    return ''.join(number)

def get_column_name():
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        col0 = 'Ссылка'
        col1 = 'Адрес'
        col2 = 'Год ввода в эксплуатацию'
        col3 = 'Детская площадка'
        col4 = 'Дом признан аварийным'
        col5 = 'Дополнительная информация'
        col6 = 'Количество жилых помещений'
        col7 = 'Класс энергетической эффективности'
        col8 = 'Количество лифтов'
        col9 = 'Количество подъездов'
        col10 = 'Лифты'
        col11 = 'Наибольшее количество этажей'
        col12 = 'Наименьшее количество этажей'
        col13 = 'Количество нежилых помещений'
        col14 = 'Площадь жилых помещений м2'
        col15 = 'Площадь нежилых помещений м2'
        col16 = 'Площадь помещений общего имущества м2'
        col17 = 'Площадь зем. участка общего имущества м2'
        col18 = 'Площадь парковки м2'
        col19 = 'Серия, тип постройки здания'
        col20 = 'Спортивная площадка'
        col21 = 'Формирование фонда кап. ремонта'
        col22 = 'Тип дома'
        col23 = 'Оборудование'
        col24 = 'Количество мусоропроводов, ед.'
        col25 = 'Несущие стены'
        col26 = 'Площадь подвала, кв.м'
        col27 = 'Крыша'
        col28 = 'Мусоропровод'
        col29 = 'Перекрытия'
        col30 = 'Фасад'
        col31 = 'Фундамент'
        col32 = 'Количество вводов в дом, ед.'
        col33 = 'Объем выгребных ям, куб. м.'
        col34 = 'Вентиляция'
        col35 = 'Водоотведение'
        col36 = 'Система водостоков'
        col37 = 'Газоснабжение'
        col38 = 'Горячее водоснабжение'
        col39 = 'Система пожаротушения'
        col40 = 'Теплоснабжение'
        col41 = 'Холодное водоснабжение'
        col42 = 'Электроснабжение'

        writer.writerow((col0,
                        col1,
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
                        col22,
                        col23,
                        col24,
                        col25,
                        col26,
                        col27,
                        col28,
                        col29,
                        col30,
                        col31,
                        col32,
                        col33,
                        col34,
                        col35,
                        col36,
                        col37,
                        col38,
                        col39,
                        col40,
                        col41,
                        col42))

def write_csv(data):
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['url_building'],
                        data['address'],
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
                        data['type_building'],
                        data['equipment'],
                        data['number_chutes'],
                        data['bearing_wall'],
                        data['square_basement'],
                        data['roof'],
                        data['refuse_chute'],
                        data['overlapping'],
                        data['facade'],
                        data['foundation'],
                        data['number_inputs'],
                        data['volume_cesspools'],
                        data['ventilation'],
                        data['water_disposal'],
                        data['drainage_system'],
                        data['gas_supply'],
                        data['hot_water_supply'],
                        data['extinguishing_system'],
                        data['heat_supply'],
                        data['cold_water_supply'],
                        data['electrosupply']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        url_building = 'http://dom.mingkh.ru' + soup.find('ul', class_='breadcrumb').find_all('li')[-1].find('a').get('href')
    except:
        url_building: '-'
    try:
        ad = soup.find('ul', class_='breadcrumb').find_all('li')[-1].find('a').text.split(',')
        address = 'Челябинск,' + ''.join(ad)
    except: 
        address = '-'
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
    equipment = '-'
    number_chutes = '-'
    bearing_wall = '-'
    square_basement = '-'
    roof = '-'
    refuse_chute = '-'
    overlapping = '-'
    facade = '-'
    foundation = '-'
    number_inputs = '-'
    volume_cesspools = '-'
    ventilation = '-'
    water_disposal = '-'
    drainage_system = '-'
    gas_supply = '-'
    hot_water_supply = '-'
    extinguishing_system = '-'
    heat_supply = '-'
    cold_water_supply = '-'
    electrosupply = '-'

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
                square_number_apartments = filter_number(tds[-1].text)

            if (tds[i].text == 'Площадь нежилых помещений м2'):
                square_number_apartments_without_people = filter_number(tds[-1].text)

            if (tds[i].text == 'Площадь помещений общего имущества м2'):
                square_common_property = filter_number(tds[-1].text)

            if (tds[i].text == 'Площадь зем. участка общего имущества м2'):
                land_square_common_property = filter_number(tds[-1].text)

            if (tds[i].text == 'Площадь парковки м2'):
                square_parking = filter_number(tds[-1].text)

            if (tds[i].text == 'Серия, тип постройки здания'):
                series_type_construction = tds[-1].text

            if (tds[i].text == 'Спортивная площадка'):
                sports_ground = tds[-1].text

            if (tds[i].text == 'Формирование фонда кап. ремонта'):
                formation_capital_repair = tds[-1].text

            if (tds[i].text == 'Тип дома'):
                type_building = tds[-1].text

            if (tds[i].text == 'Оборудование'):
                equipment = tds[-1].text

            if (tds[i].text == 'Количество мусоропроводов, ед.'):
                number_chutes = tds[-1].text

            if (tds[i].text == 'Несущие стены'):
                bearing_wall = tds[-1].text

            if (tds[i].text == 'Площадь подвала, кв.м'):
                square_basement = filter_number(tds[-1].text)

            if (tds[i].text == 'Крыша'):
                roof = tds[-1].text

            if (tds[i].text == 'Мусоропровод'):
                refuse_chute = tds[-1].text

            if (tds[i].text == 'Перекрытия'):
                overlapping = tds[-1].text

            if (tds[i].text == 'Фасад'):
                facade = tds[-1].text

            if (tds[i].text == 'Фундамент'):
                foundation = tds[-1].text

            if (tds[i].text == 'Количество вводов в дом, ед.'):
                number_inputs = tds[-1].text

            if (tds[i].text == 'Объем выгребных ям, куб. м.'):
                volume_cesspools = tds[-1].text

            if (tds[i].text == 'Вентиляция'):
                ventilation = tds[-1].text

            if (tds[i].text == 'Водоотведение'):
                water_disposal = tds[-1].text

            if (tds[i].text == 'Система водостоков'):
                drainage_system = tds[-1].text

            if (tds[i].text == 'Газоснабжение'):
                gas_supply = tds[-1].text

            if (tds[i].text == 'Горячее водоснабжение'):
                hot_water_supply = tds[-1].text

            if (tds[i].text == 'Система пожаротушения'):
                extinguishing_system = tds[-1].text

            if (tds[i].text == 'Теплоснабжение'):
                heat_supply = tds[-1].text

            if (tds[i].text == 'Холодное водоснабжение'):
                cold_water_supply = tds[-1].text

            if (tds[i].text == 'Электроснабжение'):
                electrosupply = tds[-1].text

            i = i + 1

    data = {'url_building': url_building,
            'address': address, 
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
            'type_building': type_building,
            'equipment': equipment,
            'number_chutes': number_chutes,
            'bearing_wall': bearing_wall,
            'square_basement': square_basement,
            'roof': roof,
            'refuse_chute': refuse_chute,
            'overlapping': overlapping,
            'facade': facade,
            'foundation': foundation,
            'number_inputs': number_inputs,
            'volume_cesspools': volume_cesspools,
            'ventilation': ventilation,
            'water_disposal': water_disposal,
            'drainage_system': drainage_system,
            'gas_supply': gas_supply,
            'hot_water_supply': hot_water_supply,
            'extinguishing_system': extinguishing_system,
            'heat_supply': heat_supply,
            'cold_water_supply': cold_water_supply,
            'electrosupply': electrosupply}

    write_csv(data) 

def main():
    get_column_name()
    pattern = 'http://dom.mingkh.ru/chelyabinskaya-oblast/chelyabinsk/houses?page={}'
    for i in range(1, 71): #71
        url = pattern.format(str(i))
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find('table', class_="table-bordered").find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            link = 'http://dom.mingkh.ru' + tds[2].find('a').get('href')
            get_page_data(get_html(link))

if __name__ == '__main__':
    main()