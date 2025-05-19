from datetime import datetime
from typing import Optional

from src.masks import get_mask_account, get_mask_card_number

SUPPORTED_CARDS = ("Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold")


def mask_account_card(type_and_number: str) -> Optional[str]:
    """Возвращает строку с замаскированным номером карты или счета."""

    type_and_number = type_and_number.strip()
    if not type_and_number:
        raise ValueError("Полученная строка не может быть пустой.")

    counter = 0
    for i in type_and_number[::-1]:
        if i.isdigit():
            counter -= 1
        else:
            break

    if counter == -20 or counter == -16:
        # Случай работы со счётом
        if counter == -20 and ("Счет" in type_and_number or "счет" in type_and_number or "Счёт" in type_and_number):
            return f'{"Счет"} {get_mask_account(type_and_number[-20:])}'
        elif counter == -20 and "Счет" not in type_and_number:
            raise ValueError('Отсутствует указатель "Счет" в начале строки.')

        # Случай работы с картой
        for card in SUPPORTED_CARDS:
            if card in type_and_number:
                if counter == -16:
                    return f"{card} {get_mask_card_number(type_and_number[-16:])}"
            elif card == SUPPORTED_CARDS[-1]:
                raise ValueError("Указан не поддерживаемый или не верный тип карты.")
    else:
        raise ValueError("Не корректные данные, указанный номер не является ни номером карты, ни счета.")

    assert False, "Сюда выполнение не должно дойти"


def get_date(date: str) -> Optional[str]:
    """
    Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'
    На вход подается строка в расширенном формате ISO 8601 с указанием даты, времени и 6 символов микросекунд.

    Пример: '2018-06-30T02:08:58.425572'
    """
    if not isinstance(date, str):
        raise TypeError("На входе получен не правильный тип данных, ожидался str.")
    date = date.strip()

    if not date:
        raise ValueError("Некорректный ввод данных: пустая строка.")
    elif len(date) != 26:
        raise ValueError("Некорректный или нестандартный формат даты.")

    try:
        if datetime.fromisoformat(date):
            return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    except ValueError:
        raise ValueError("Некорректный ввод данных: строка не является допустимой датой и временем.")

    assert False, "Сюда выполнение не должно дойти"