from typing import Iterable


def filter_by_currency(transactions_data: list[dict], currency: str) -> Iterable[dict]:
    for transaction in transactions_data:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
