from typing import List, Dict, Any, Iterator


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Функция принимает на вход список словарей "transactions_list", представляющих транзакции в следующем формате.

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
