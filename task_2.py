import re
import csv
import json
import yaml

"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
    и формирующий новый «отчетный» файл в формате CSV. Для этого:

    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных 
    данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
    os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
    в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
    в файл main_data (также для каждого файла);
    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(),
    а также сохранение подготовленных данных в соответствующий CSV-файл;
    Проверить работу программы через вызов функции write_to_csv().
"""

paths = [
    'info_1.txt',
    'info_2.txt',
    'info_3.txt',
]

def get_data(*args):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [
        [
            'Изготовитель системы',
            'Название ОС',
            'Код продукта',
            'Тип системы',
        ],
    ]

    for path in args:
        with open(path, encoding='cp1251') as f:
            data = f.read()
            pattern = r'( *)([\S].*)(\n)'
            os_prod_list.append(re.search(r'(Изготовитель системы:)' + pattern, data).group(3))
            os_name_list.append(re.search(r'(Название ОС:)' + pattern, data).group(3))
            os_code_list.append(re.search(r'(Код продукта:)' + pattern, data).group(3))
            os_type_list.append(re.search(r'(Тип системы:)' + pattern, data).group(3))
    
    for prod, name, code, os_type in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
        main_data.append([prod, name, code, os_type])

    return main_data

def write_to_csv(*args, path='temp.csv'):
    with open(path, 'w') as f:
        csv_f =csv.writer(f)
        csv_f.writerows(get_data(*args))


# write_to_csv(*paths, path='temp.csv')

"""    
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его
    заполнение данными. Для этого:

    Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer),
    дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных
    символа;
    Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
def write_order_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r') as f:
        orders_dict = json.load(f)

        orders_dict['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })

    with open('orders.json', 'w') as f:
        json.dump(orders_dict, f, indent=4)


# write_order_json('sour',3,'100$', 'username', '20-12-22')


"""  
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:

    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь,
    где знач-ение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра
    default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""


def write_to_yaml(some_dict):
    with open('file.yaml', 'w') as f:
        yaml.dump(some_dict, f, default_flow_style=True, allow_unicode=True)


prepared_data = {
    'first_key': ['first_value', 'second_value', 123, 255,],
    'second_key': 55,
    'third_key': {
        'currency': '100€',
        'billing': '100$',
    }
}

write_to_yaml(prepared_data)