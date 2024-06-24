def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты"""

    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"


def get_mask_account(account_num: str) -> str:
    """Возвращает маску номера счета"""

    return f"**{account_num[-4:]}"
