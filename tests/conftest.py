import pytest


@pytest.fixture
def transactions():
    list_ = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return list_


@pytest.fixture
def transactions_stateless():
    list_ = [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}
    ]
    return list_


@pytest.fixture
def maestro_card():
    return "Maestro 7000792289606361"


@pytest.fixture
def transactions_full_info():
    list_ = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 275389102,
            "state": "EXECUTED",
            "date": "2020-11-15T14:52:17.987654",
            "operationAmount": {
                "amount": "5678.90",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Оплата услуг",
            "from": "Счет 42768295301234567890",
            "to": "Счет 40702810000000000001"
        },
        {
            "id": 849201653,
            "state": "CANCELED",
            "date": "2021-08-22T09:31:42.123456",
            "operationAmount": {
                "amount": "12345.67",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод между счетами",
            "from": "Счет 98765432109876543210",
            "to": "Счет 12345678901234567890"
        },
        {
            "id": 512345678,
            "state": "EXECUTED",
            "date": "2022-03-10T18:05:00.543210",
            "operationAmount": {
                "amount": "999.99",
                "currency": {
                    "name": "GBP",
                    "code": "GBP"
                }
            },
            "description": "Покупка в интернет-магазине",
            "from": "Счет 55556666777788889999",
            "to": "Счет 11223344556677889900"
        },
        {
            "id": 398765432,
            "state": "EXECUTED",
            "date": "2023-01-28T05:10:30.789012",
            "operationAmount": {
                "amount": "1500.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Пополнение счета",
            "from": "Счет 88889999000011112222",
            "to": "Счет 33334444555566667777"
        }
    ]
    return list_


@pytest.fixture
def card_numbers():
    list_ = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    return list_
