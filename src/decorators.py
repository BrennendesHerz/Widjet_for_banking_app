from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор для логирования результатов выполнения функции"""

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> None:
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"Фуккция {function.__name__} выполнена с результатом {result}\n")

                else:
                    print(f"Фуккция {function.__name__} выполнена с результатом {result}")

            except Exception as err:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} erroer: {err}. Inputs: {args}, {kwargs}\n")

                else:
                    print(f"{function.__name__} erroer: {err}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper
