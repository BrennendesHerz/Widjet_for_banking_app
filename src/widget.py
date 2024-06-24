from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_account_card: str) -> str:
    """Возвращает маску номера карты/счета в зависимости от входного значения"""

    if "счет" in info_account_card.lower():
        account_info_split = info_account_card.split(" ")
        return f"{account_info_split[0]} {get_mask_account(account_info_split[1])}"
    else:
        card_info_split = info_account_card.split(" ")
        return f"{' '.join(card_info_split[:-1])} {get_mask_card_number(card_info_split[-1])}"
