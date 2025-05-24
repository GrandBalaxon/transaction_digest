def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX, где X — это цифра номера."""
    if card_number is None:
        raise ValueError("Номер карты не может быть пустым.")

    if isinstance(card_number, int):
        card_number = str(card_number)
    elif isinstance(card_number, str):
        card_number = card_number.replace(" ", "")
    else:
        raise TypeError("Номер карты должен быть строкой или целым числом.")

    # Проверяем на пустую строку после преобразований
    if not card_number:
        raise ValueError("Номер карты не может быть пустым.")

    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр.")

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(acc_number: str | int) -> str:
    """Маскирует номер счета в формате **XXXX, где `X` — это цифра номера."""

    if isinstance(acc_number, int):
        acc_number = str(acc_number)
    elif isinstance(acc_number, str):
        acc_number = acc_number.replace(" ", "")
    else:
        raise TypeError("Номер счета должен быть строкой или целым числом.")

    if not acc_number.isdigit():
        raise ValueError("Номер аккаунта должен состоять только из цифр.")
    if len(acc_number) != 20:
        raise ValueError("Номер аккаунта должен содержать ровно 20 цифр.")

    return f"**{acc_number[-4:]}"
