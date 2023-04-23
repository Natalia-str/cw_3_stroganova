import json
import time
from datetime import datetime
json_file = 'operations.json'

def get_data(json_file):
    """Получает данные из файла .json"""

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    """Принимает данные и фильтрует их. Возвращает данные только с выполненными операциями"""
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

def sort_data(data):
    """Сортирует данные по последней дате. Возвращает 5 последних операций """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[0:5]

def formate_data(data):
    """Принимает список словарей. Форматирует дату. Форматирует данные. Возвращает список
    отформатированных данных"""
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        if "from" in row:
            from_arrow = " -> "
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f' {sender_bill[:4]} {sender_bill[4:6]} ** **** {sender_bill[-4:]}'

        else:
            from_arrow = ""
            sender_info = ""
            sender_bill = ""

        to = row['to'].split()
        to_count = to.pop(-1)
        to_count = f'**{to_count[-2:]}'
        to_info = " ".join(to)
        amount = row['operationAmount']['amount']
        currency = row['operationAmount']['currency']['name']

        formatted_data.append(f"""{date} {description}
{sender_info}{sender_bill}{from_arrow}{to_info} {to_count}
{amount} {currency}
        """)

    return formatted_data
