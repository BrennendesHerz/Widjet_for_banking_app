def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список операций, статус которых соответствует переданному в функцию"""

    list_by_state = []
    for data_dict in data_list:
        if data_dict["state"] == state:
            list_by_state.append(data_dict)
    return list_by_state
