from datetime import datetime


def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список операций, статус которых соответствует переданному в функцию"""

    list_by_state = []
    for data_dict in data_list:
        if data_dict["state"] == state:
            list_by_state.append(data_dict)
    return list_by_state


def sort_by_date(data_list: list[dict], is_sort_reverse: bool = True) -> list[dict]:
    """Возвращает новый список, в котором исходные словари отсортированы по датам"""

    return sorted(
        data_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=is_sort_reverse
    )
