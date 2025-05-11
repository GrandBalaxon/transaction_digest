import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    (7000792289606361, "7000 79** **** 6361"),
    ("0000000000000000", "0000 00** **** 0000"),
    (9999999999999999, "9999 99** **** 9999")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_error_1(maestro_card):
    with pytest.raises(ValueError, match="Номер карты должен состоять только из цифр."):
        get_mask_card_number(maestro_card)


def test_get_mask_card_number_error_2(card_number="410000007769"):
    with pytest.raises(ValueError, match="Номер карты должен содержать ровно 16 цифр."):
        get_mask_card_number(card_number)


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError, match="Номер карты не может быть пустым."):
        get_mask_card_number('')


def test_get_mask_card_number_type_error():
    with pytest.raises(TypeError, match="Номер карты должен быть строкой или целым числом."):
        get_mask_card_number(222233334444.5555)


@pytest.mark.parametrize("acc_number, expected", [
    ("73654108430135874305", "**4305"),
    (73654108430135874305, "**4305"),
    (" 73654108430135874305 ", "**4305")
])
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected


def test_get_mask_account_not_digits():
    with pytest.raises(ValueError, match="Номер аккаунта должен состоять только из цифр."):
        get_mask_account("fuheriuhg854y6t")


def test_get_mask_account_wrong_length():
    with pytest.raises(ValueError, match="Номер аккаунта должен содержать ровно 20 цифр."):
        get_mask_account("567084057")


def test_get_mask_account_type_error():
    with pytest.raises(TypeError, match="Номер счета должен быть строкой или целым числом."):
        get_mask_account(2222.99)
