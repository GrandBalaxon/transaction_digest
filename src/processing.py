from typing import List, Dict, Any


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей на основе значения ключа 'state'."""
    return [i for i in list_of_dicts if i["state"] == state]


def sort_by_date(list_of_dicts: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    descending: True (по умолчанию) - сортировка по убыванию (от новых к старым).
                False - сортировка по возрастанию (от старых к новым).
    """
    return sorted(list_of_dicts, key=lambda x: x["date"][:10], reverse=descending)


if __name__ == "__main__":
    test_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    list_ = sort_by_date(test_list)
    for i in list_:
        print(i)
