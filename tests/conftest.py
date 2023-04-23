import pytest
import json

@pytest.fixture
def test_data():
    return [
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        },
        {
            "id": 476991061,
            "state": "CANCELED",
            "date": "2017-11-23T17:47:33.127140",
            "operationAmount": {
                "amount": "26971.25",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 7305799447374042",
            "to": "Maestro 3364923093037194"
        },
        {
            "id": 633268359,
            "state": "EXECUTED",
            "date": "2019-07-12T08:11:47.735774",
            "operationAmount": {
                "amount": "2631.44",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 3589276410671603",
            "to": "Счет 96292138399386853355"
        },
    ]

@pytest.fixture
def test_path():
    json_file = "test_data.json"
    return json_file
