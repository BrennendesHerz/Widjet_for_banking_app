from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    input_card_num = input("Введите номер карты: ")
    print(get_mask_card_number(input_card_num))

    input_account_num = input("Введите номер счета: ")
    print(get_mask_account(input_account_num))
