def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список операций, статус которых соответствует переданному в функцию"""

    list_by_state = []
    for data_dict in data_list:
        if data_dict["state"] == state:
            list_by_state.append(data_dict)
    return list_by_state


def sort_by_date(data_list: list[dict], sort_reverse: bool = True) -> list[dict]:
    """Возвращает новый список, в котором исходные словари отсортированы по датам"""

    if sort_reverse:
        return sorted(data_list, key=lambda x: ".".join(x["date"][:10].split("-")), reverse=True)
    else:
        return sorted(data_list, key=lambda x: ".".join(x["date"][:10].split("-")))
