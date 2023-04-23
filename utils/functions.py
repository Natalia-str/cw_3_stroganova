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

