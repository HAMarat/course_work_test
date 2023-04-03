import json
import datetime
import sys


def get_data_json(file_name: str) -> list:
    """
    Функция для загрузки данных из json файла
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)
    return data


def filter_data_by_state(data: list[dict], state: str) -> filter | None:
    """
    Функция для фильтрации операции
    """
    return filter(lambda x: x.get("state") == state, data)


def sorted_data_by_date(data: filter, key, reverse=True) -> list[dict]:
    """
    Функция для сортировки операции
    """
    return sorted(data, key=lambda x: x.get(key), reverse=reverse)


def get_date(operation: dict) -> str:
    """
    Функция для преобразования даты
    """
    date = operation.get('date')
    if date:
        date_formate = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_formate.strftime("%d.%m.%Y")


def get_from(operation: dict) -> str:
    """
    Функция для преобразования счета отправления
    """
    data_from = operation.get('from')
    if data_from:
        data_with_secret = get_data_secret(data_from)
        return data_with_secret + ' -> '
    return ''


def get_data_secret(data: str) -> str:
    """
    Функция для скрытия информации
    """
    split_data = data.split(" ")

    if 'Счет' in split_data:
        split_data[-1] = f'**{split_data[-1][-5:-1]}'
    else:
        split_data[-1] = f'{split_data[-1][0:5]} {split_data[-1][5:7]}** **** {split_data[-1][-5:-1]}'
    return ' '.join(split_data)


def return_data(data: list[dict]) -> list:
    """
    Функция для подготовки данных для вывода информации
    """
    result = []
    for operation in data:
        get_date(operation)
        return_operation = (
            f"{get_date(operation)} {operation.get('description')}\n"
            f"{get_from(operation)}{get_data_secret(operation.get('to'))}\n"
            f"{operation.get('operationAmount').get('amount')} "
            f"{operation.get('operationAmount').get('currency').get('name')}"
        )
        result.append(return_operation)
    return result
