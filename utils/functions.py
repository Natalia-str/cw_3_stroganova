import json
import time
from datetime import datetime
json_file = 'operations.json'

def get_data(json_file):
    """Получает данные из файла .json"""

    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
