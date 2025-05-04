from typing import Any, Dict, List


def filter_by_state(transactions_list: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей на основе значения ключа 'state'."""
    return [i for i in transactions_list if i["state"] == state]


def sort_by_date(transactions_list: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    descending: True (по умолчанию) - сортировка по убыванию (от новых к старым).
                False - сортировка по возрастанию (от старых к новым).
    """
    if len(transactions_list[0]["date"]) != 26:
        raise ValueError(
            """
        Некорректный или нестандартный формат дат.
        Используйте расширенный формат ISO 8601 с указанием даты, времени и микросекунд.
        """
        )

    return sorted(transactions_list, key=lambda x: x["date"], reverse=descending)
