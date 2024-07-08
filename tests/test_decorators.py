from typing import Any

from src.decorators import log


def test_log_without_filename_on_positive(capsys: Any) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "Фуккция add выполнена с результатом 3\n"


def test_log_without_filename_on_negative(capsys: Any) -> None:
    @log()
    def add(x: Any, y: Any) -> Any:
        return x + y

    add(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "add erroer: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"


def test_log_with_filename_on_positive() -> None:
    @log(filename="mylog.txt")
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    with open("mylog.txt", "r") as file:
        last_record = file.readlines()[-1]
    assert last_record == "Фуккция add выполнена с результатом 3\n"


def test_log_with_filename_on_negative() -> None:
    @log(filename="mylog.txt")
    def add(x: Any, y: Any) -> Any:
        return x + y

    add(1, "2")
    with open("mylog.txt", "r") as file:
        last_record = file.readlines()[-1]
    assert last_record == "add erroer: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"
