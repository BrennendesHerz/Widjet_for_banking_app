from typing import Iterable


def filter_by_currency(transactions_data: list[dict], currency: str) -> Iterable:
    for transaction in transactions_data:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_data: list[dict]) -> Iterable:
    for transaction in transactions_data:
        yield transaction["description"]


def card_number_generator(init_value: int, final_value: int) -> Iterable:
    if 1 <= init_value and init_value <= final_value <= 9999999999999999:
        for num in range(init_value, final_value + 1):
            r = str(num).zfill(16)
            yield f"{r[:4]} {r[4:8]} {r[8:12]} {r[12:]}"
    else:
        yield "Введены некорректные значения"
