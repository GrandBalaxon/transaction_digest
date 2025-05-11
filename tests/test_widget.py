import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("type_and_number, expected", [
    ("Счет 73654108430135874305", "Счет **4305"),
    ("счет64686473678894779589", "Счет **9589"),
    ("Счёт 64686473678894779589", "Счет **9589"),
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    (" Maestro 1596837868705199    ", "Maestro 1596 83** **** 5199")
])
def test_mask_account_card(type_and_number, expected):
    assert mask_account_card(type_and_number) == expected


def test_mask_account_card_wrong_type_of_a_card():
    with pytest.raises(ValueError, match="Указан не поддерживаемый или не верный тип карты."):
        mask_account_card("Мир 2200770212727079")


def test_mask_account_card_wrong_numeric_value():
    with pytest.raises(ValueError, match="Не корректные данные, указанный номер не является ни номером карты, ни счета."):
        mask_account_card("Мир 22007702127270")


def test_mask_account_card_empty_input():
    with pytest.raises(ValueError, match="Полученная строка не может быть пустой."):
        mask_account_card("")


def test_mask_account_card_acc_indication_absence():
    with pytest.raises(ValueError, match='Отсутствует указатель "Счет" в начале строки.'):
        mask_account_card("73654108430135874305")


@pytest.mark.parametrize("date_data, expected", [
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2018-09-12T21:27:25.241689", "12.09.2018")
])
def test_get_date(date_data, expected):
    assert get_date(date_data) == expected


def test_get_date_wrong_format():
    with pytest.raises(ValueError, match="Некорректный или нестандартный формат даты."):
        get_date("Tue, 1 Jul 2008 10:52:37 +0530")


def test_get_date_empty_string():
    with pytest.raises(ValueError, match="Некорректный ввод данных: пустая строка."):
        get_date("")


def test_get_date_not_real_date():
    with pytest.raises(ValueError, match="Некорректный ввод данных: строка не является допустимой датой и временем."):
        get_date("2018-13-12T21:27:25.241689")


def test_get_date_type_error():
    with pytest.raises(TypeError, match="На входе получен не правильный тип данных, ожидался str."):
        get_date(88005553535)
