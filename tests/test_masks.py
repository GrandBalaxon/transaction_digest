import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000 7922 8960 6361", "7000 79** **** 6361"),
    (7000792289606361, "7000 79** **** 6361")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_error_1(maestro_card):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(maestro_card)

    assert str(exc_info.value) == "Номер карты должен состоять только из цифр."


def test_get_mask_card_number_error_2(card_number="410000007769"):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)

    assert str(exc_info.value) == "Номер карты должен содержать ровно 16 цифр."


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('')

    assert str(exc_info.value) == "Номер карты не может быть пустым."


def test_get_mask_card_number_type_error():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(222233334444.5555)

    assert str(exc_info.value) == "Номер карты должен быть строкой или целым числом."