from utils import functions
import json


def test_get_data(test_path):
    gotten_data = functions.get_data(test_path)
    assert len(gotten_data) > 0


def test_filter_data(test_data):
    filtered_data = functions.filter_data(test_data)
    assert [x['state'] for x in filtered_data] == ['EXECUTED', 'EXECUTED']


def test_sort_data(test_data):
    sorted_data = functions.sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-12T08:11:47.735774', '2018-12-28T23:10:35.459698', '2017-11-23T17:47:33.127140']


def test_formate_data(test_data):
    formated_data = functions.formate_data(test_data)
    assert [x for x in formated_data] == ['28.12.2018 Открытие вклада\nСчет **91\n49192.52 USD\n        ',
 '23.11.2017 Перевод с карты на карту\n'
 'Visa Gold 7305 79 ** **** 4042 -> Maestro **94\n'
 '26971.25 руб.\n'
 '        ',
 '12.07.2019 Перевод организации\n'
 'Visa Gold 3589 27 ** **** 1603 -> Счет **55\n'
 '2631.44 руб.\n'
 '        ']
