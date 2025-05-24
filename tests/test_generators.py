import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_usd_currency(transactions_full_info):
    """Тестирования результатов с валютой USD."""
    temp_transactions_list = filter_by_currency(transactions_full_info, "USD")
    expected = (
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
        }
    )
    i = 0

    while True:
        try:
            assert next(temp_transactions_list) == expected[i]
            i += 1
        except StopIteration:
            break


def test_filter_by_rub_currency(transactions_full_info):
    """Тестирование результатов с валютой RUB."""
    temp_transactions_list = filter_by_currency(transactions_full_info, "RUB")
    expected = (
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
    )
    i = 0

    while True:
        try:
            assert next(temp_transactions_list) == expected[i]
            i += 1
        except StopIteration:
            break


def test_filter_by_currency_empty_list_case():
    """Тестируем работу с пустым списком."""
    list_ = []
    with pytest.raises(ValueError, match="На вход не получен список словарей нужного формата."):
        iterator = filter_by_currency(list_, "USD")
        next(iterator)


def test_filter_by_currency_non_found_currency(transactions_full_info):
    """
    На вход подаем не существующую в списке словарей валюту.
    Ожидается отсутствие итераторов и мгновенная ошибка StopIterator.
    """
    iterator = filter_by_currency(transactions_full_info, "CNY")
    with pytest.raises(StopIteration):
        next(iterator)


def test_filter_by_currency_wrong_list_format(transactions_stateless):
    """
    Тест работы с неправильным форматом словаря на входе.
    Сообщение об ошибке дополнительно обрамляется кавычками '', т.к KeyError.
    """
    iterator = filter_by_currency(transactions_stateless, "USD")
    with pytest.raises(KeyError, match="'На вход не получен список словарей нужного формата.'"):
        next(iterator)


@pytest.mark.parametrize("i, expected",
                         [
                             (0, "Перевод организации"),
                             (1, "Перевод со счета на счет"),
                             (2, "Оплата услуг"),
                             (3, "Перевод между счетами"),
                             (4, "Покупка в интернет-магазине"),
                             (5, "Пополнение счета")
                          ],
                         )
def test_transaction_descriptions(transactions_full_info, i, expected):
    """
    Тестирование работы со списком в фикстуре.
    Ожидается правильная выдача значений в нужном порядке.
    """
    iterator = transaction_descriptions(transactions_full_info)
    list_of_expected = [x["description"] for x in transactions_full_info]
    index = 0
    while True:
        try:
            if index == i:
                assert next(iterator) == list_of_expected[i]
            next(iterator)
            index += 1
        except StopIteration:
            break


def test_transaction_descriptions_empty_list_case():
    """Тестирование работы с пустым списком."""
    list_ = []
    with pytest.raises(ValueError, match="На вход не получен список словарей нужного формата."):
        iterator = transaction_descriptions(list_)
        next(iterator)


def test_transaction_descriptions_wrong_list_format(transactions_stateless):
    """
    Тест работы с неправильным форматом словаря на входе.
    Сообщение об ошибке дополнительно обрамляется кавычками '', т.к KeyError.
    """
    iterator = transaction_descriptions(transactions_stateless)
    with pytest.raises(KeyError, match="'На вход не получен список словарей нужного формата.'"):
        next(iterator)


@pytest.mark.parametrize("start, finish", [
    (1, 5),
    (5, 1),
    ("0000 0000 0000 0001", "0000 0000 0000 0005"),
    (1, "0000 0000 0000 0005")
])
def test_card_number_generator(card_numbers, start, finish):
    """Тестируем совпадение значений от 1 до 5 при различных входных данных."""
    i = 0
    iterator = card_number_generator(start, finish)
    while True:
        try:
            assert next(iterator) == card_numbers[i]
            i += 1
        except StopIteration:
            break


def test_card_number_generator_big_values():
    """Тестируем работу функции с реальным примером карт, первые 8 цифр не 0."""
    list_ = [
        "5469 4100 0000 0005",
        "5469 4100 0000 0006",
        "5469 4100 0000 0007",
        "5469 4100 0000 0008"
    ]
    i = 0
    iterator = card_number_generator("5469 4100 0000 0005", "5469 4100 0000 0008")
    while True:
        try:
            assert next(iterator) == list_[i]
            i += 1
        except StopIteration:
            break


@pytest.mark.parametrize("start, finish", [
    (-1, 10),
    ("9999 9999 9999 9998", 9999999999999999 + 1)
])
def test_card_number_generator_out_of_boundaries(start, finish):
    """Тесты на случаи выхода из допустимого диапазона."""
    with pytest.raises(
            ValueError,
            match="Заданные числа должны находиться в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."
    ):
        iterator = card_number_generator(start, finish)
        print(next(iterator))


def test_card_number_generator_invalid_str_input():
    with pytest.raises(
            ValueError,
            match="Строки в значениях start / finish содержат не допустимые символы."
    ):
        iterator = card_number_generator("-1a.", 10)
        print(next(iterator))


def test_card_number_generator_type_error():
    with pytest.raises(TypeError, match="На входе получены не допустимые типы данных."):
        iterator = card_number_generator(["-1a."], 10)
        print(next(iterator))
