from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей на основе значения ключа 'state'."""

    try:
        for index, dict_ in enumerate(transactions_list):
            if "state" not in dict_:
                raise KeyError(f"В словаре с индексом {index} отсутствует ключ state.")

        return [i for i in transactions_list if i["state"] == state]
    except TypeError:
        raise TypeError("На входе получен не правильный тип данных.")


def sort_by_date(transactions_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Формат дат - расширенный ISO 8601 с указанием даты, времени и 6 символов микросекунд.
    Пример: '2018-06-30T02:08:58.425572'

    descending: True (по умолчанию) - сортировка по убыванию (от новых к старым).
                False - сортировка по возрастанию (от старых к новым).
    """

    # Проверка списка словарей на правильность записей дат
    for index, data in enumerate(transactions_list):
        if not isinstance(data["date"], str):
            raise TypeError(f"Строка {data['date']} словаря по индексу {index} имеет не правильный тип данных.")
        elif len(data["date"]) != 26:
            raise ValueError(
                f"Некорректный или нестандартный формат даты {data["date"]} в словаре по индексу {index}."
            )
        try:
            datetime.fromisoformat(data["date"])
        except ValueError:
            raise ValueError(
                f"Строка {data['date']} словаря по индексу {index} не является реальной датой и временем."
            )

    return sorted(transactions_list, key=lambda x: x["date"], reverse=descending)
