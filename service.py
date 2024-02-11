import json


def read_keys_from_json_file(filename: str) -> list:
    """
    Достает ключи из файла json

    :param filename: имя файла
    """
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
        if data:
            return list(data[0].keys())
        else:
            return []


def validate_phone_number(key: int):
    """
    Проверяет валидность номера телефона.

    :param key: Номер телефона для проверки.
    :return: True, если номер телефона валиден, иначе False
    """
    while True:
        phone_number = input(f"{key} - ")
        if phone_number.isdigit():
            return phone_number
        else:
            print("Номер должен состоять из чисел")
