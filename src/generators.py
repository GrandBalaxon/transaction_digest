from typing import Any, Dict, Iterator, List, Union


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Функция-генератор которая принимает на вход список словарей "transactions_list" в следующем формате.

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
    }

    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной "currency" (например, USD).
    """
    if not transactions_list:
        raise ValueError("На вход не получен список словарей нужного формата.")

    try:
        filtered_list = filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list)
        for transaction in filtered_list:
            yield transaction
    except KeyError:
        raise KeyError("На вход не получен список словарей нужного формата.")


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Функция-генератор которая принимает список словарей с транзакциями "transactions_list" формата.

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
    }

    Возвращает генератор выдающий описание каждой операции по очереди.
    """
    if not transactions_list:
        raise ValueError("На вход не получен список словарей нужного формата.")

    try:
        for transaction in transactions_list:
            yield transaction["description"]
    except KeyError:
        raise KeyError("На вход не получен список словарей нужного формата.")


def card_number_generator(start: Union[int, str], finish: Union[int, str]) -> Iterator[str]:
    """
    Функция-генератор который выдает номера банковских карт в формате "XXXX XXXX XXXX XXXX", где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генерация значений происходит от меньшего к большому.

    На start и finish подаются строковые или численные значения.
    При указывании значения от большего к меньшему - функция всё равно отработает как полагается, поменяв их местами.
    """
    # Проверка на тип str
    try:
        if isinstance(start, str):
            start = int(start.replace(" ", ""))
        if isinstance(finish, str):
            finish = int(finish.replace(" ", ""))
    except ValueError:
        raise ValueError("Строки в значениях start / finish содержат не допустимые символы.")

    try:
        # Если start > finish то меняем их местами
        if start > finish:
            start, finish = finish, start

        # Проверка на соответствие старта и финиша необходимому диапазону
        if not (1 <= start <= 9999999999999999) or not (1 <= finish <= 9999999999999999):
            raise ValueError(
                "Заданные числа должны находиться в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."
            )

        for card_number in range(start, finish + 1):
            str_card_number = str(card_number)
            full_str_cd_num = (16 - len(str_card_number)) * "0" + str_card_number

            yield f"{full_str_cd_num[:4]} {full_str_cd_num[4:8]} {full_str_cd_num[8:12]} {full_str_cd_num[12:]}"

    except TypeError:
        raise TypeError("На входе получены не допустимые типы данных.")
