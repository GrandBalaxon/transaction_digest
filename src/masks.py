def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""

    if isinstance(card_number, int):
        card_number = str(card_number)
    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр.")
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(acc_number: str | int) -> str:
    """Маскирует номер счета в формате **XXXX."""

    if isinstance(acc_number, int):
        acc_number = str(acc_number)
    if not acc_number.isdigit():
        raise ValueError("Номер аккаунта должен состоять только из цифр.")
    if len(acc_number) != 20:
        raise ValueError("Номер аккаунта должен содержать ровно 20 цифр.")

    return f"**{acc_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361), get_mask_account(73654108430135874305), sep="\n")
