import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("account_card_num, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                              ("Счет 64686473678894779589", "Счет **9589"),
                                              ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                              ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(account_card_num, expected):
    assert mask_account_card(account_card_num) == expected


@pytest.mark.parametrize("transaction_info, expected", [("2018-07-11T02:26:18.671407", "11.07.2018"),
                                              ("2019-07-03T18:35:29.512364", "03.07.2019"),
                                              ("2018-06-30T02:08:58.425572", "30.06.2018")])
def test_get_data(transaction_info, expected):
    assert get_data(transaction_info) == expected