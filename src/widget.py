from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета."""
    temp_list = type_and_number.split()

    if temp_list[-1].isdigit() and len(temp_list[-1]) == 16:
        temp_list[-1] = get_mask_card_number(temp_list[-1])
    elif temp_list[-1].isdigit() and len(temp_list[-1]) == 20:
        temp_list[-1] = get_mask_account(temp_list[-1])

    return " ".join(temp_list)


def get_date(date: str) -> str:
    """Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


if __name__ == "__main__":
    print(
        get_mask_card_number(7000792289606361),
        get_mask_account(73654108430135874305),
        mask_account_card("Счет 73654108430135874305"),
        get_date("2024-03-11T02:26:18.671407"),
        sep="\n",
    )
