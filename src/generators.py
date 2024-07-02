from typing import Iterable


def filter_by_currency(transactions_data: list[dict], currency: str) -> Iterable:
    for transaction in transactions_data:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_data: list[dict]) -> Iterable:
    for transaction in transactions_data:
        yield transaction["description"]
