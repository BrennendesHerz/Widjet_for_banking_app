from typing import Iterable


def filter_by_currency(transactions_data: list[dict], currency: str) -> Iterable:
    """Поочередно возвращает всю информацию о транзакциях с заданной валютой"""

    if isinstance(transactions_data, list):
        if transactions_data:
            for transaction in transactions_data:
                if "operationAmount" in transaction and "currency" in transaction["operationAmount"]:
                    if transaction.get("operationAmount").get("currency").get("code") == currency:
                        yield transaction
    while True:
        yield "Данные о транзакциях отсутствуют"


def transaction_descriptions(transactions_data: list[dict]) -> Iterable:
    """Поочередно возвращает описание транзакций"""

    if isinstance(transactions_data, list):
        if transactions_data:
            for transaction in transactions_data:
                if type(transaction) is dict:
                    yield transaction.get("description")
    while True:
        yield "Данные о транзакциях отсутствуют"


def card_number_generator(init_value: int, final_value: int) -> Iterable:
    """Генерирует номера карт в заданном диапазоне в формате ХХХХ ХХХХ ХХХХ ХХХХ"""

    if 1 <= init_value and init_value <= final_value <= 9999999999999999:
        for num in range(init_value, final_value + 1):
            r = str(num).zfill(16)
            yield f"{r[:4]} {r[4:8]} {r[8:12]} {r[12:]}"
    else:
        yield "Введены некорректные значения"
