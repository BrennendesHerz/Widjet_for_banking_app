import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_with_correct_arg(extended_transaction_data):
    generator = filter_by_currency(extended_transaction_data, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_less_correct_arg(extended_transaction_data):
    # Передача в функцию отсутствующей валюты
    generator = filter_by_currency(extended_transaction_data, "EUR")
    assert next(generator) == "Данные о транзакциях отсутствуют"

    # Передача в функцию пустого списка
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Данные о транзакциях отсутствуют"

    # Передача списка без нужных ключей
    generator = filter_by_currency(["USD", "RUB", "EUR"], "RUB")
    assert next(generator) == "Данные о транзакциях отсутствуют"


def test_transaction_descriptions_with_correct_arg(extended_transaction_data):
    generator = transaction_descriptions(extended_transaction_data)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "data_list, expected",
    [([], "Данные о транзакциях отсутствуют"), (["USD", "RUB", "EUR"], "Данные о транзакциях отсутствуют")],
)
def test_transaction_descriptions_less_correct_arg(data_list, expected):
    generator = transaction_descriptions(data_list)
    assert next(generator) == expected


def test_card_number_generator_with_correct_arg():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"

    generator = card_number_generator(8987456512320258, 8987456512320259)
    assert next(generator) == "8987 4565 1232 0258"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (0, 5, "Введены некорректные значения"),
        (5, 99999999999999999, "Введены некорректные значения"),
        (5, 4, "Введены некорректные значения"),
    ],
)
def test_card_number_generator_less_correct_arg(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
