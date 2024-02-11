import json
from service import read_keys_from_json_file, validate_phone_number


class PhoneBook:
    def __init__(self, file_name: str, encoding: str = 'utf-8'):
        """
        Создает объект телефонной книги.

        :param file_name: Имя файла для хранения данных
        :param encoding: Кодировка файла
        """
        self.file_name = file_name
        self.encoding = encoding

    def display_data(self, page_size: int = 1):
        """
        Выводит записи из телефонной книги постранично.

        :param page_size: Количество записей на одной странице
        """
        try:
            with open(self.file_name, "r", encoding=self.encoding) as file:
                data = json.load(file)
                num_entries = len(data)  # общее количество записей
                num_pages = (num_entries + page_size - 1) // page_size  # общее количество странице

                while True:
                    page_num = input("Введите номер страницы (для выхода введите 'q'): ")
                    if page_num.lower() == 'q':
                        return ""

                    if not page_num.isdigit() or int(page_num) < 1 or int(page_num) > num_pages:
                        print("Некорректный номер страницы. Пожалуйста, введите число от 1 до", num_pages)
                        continue

                    start_index = (int(page_num) - 1) * page_size
                    end_index = min(start_index + page_size, num_entries)
                    page_entries = data[start_index:end_index]
                    print("\nЗаписи на странице", page_num + ":")
                    for entry in page_entries:
                        print("---------")
                        for key, value in entry.items():
                            print(f"{key}: {value}")
        except json.JSONDecodeError:
            print("В книге нет записей.")
            return ""

    def add_data(self):
        """Добавляет записи в справочник."""
        keys = read_keys_from_json_file(self.file_name)
        new_entry = {}
        print("Введите следующие данные:")
        for key in keys:
            if key == 'work_phone' or key == 'personal_phone':
                new_entry[key] = validate_phone_number(key)
            else:
                new_entry[key] = input(f"{key} - ")
        with open(self.file_name, "r+", encoding=self.encoding) as file:
            data = json.load(file)
            data.append(new_entry)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=2)
            file.truncate()
            print("Запись успешно добавлена")
        return ""

    def change_entry(self):
        """Редактирование контакта, соответствующего заданному поисковому термину."""
        try:
            with open(self.file_name, "r+", encoding=self.encoding) as file:
                data = json.load(file)
                num_entries = len(data)
                entry_id = int(input("Введите номер записи: "))
                if entry_id < 1 or entry_id > num_entries:
                    print("Некорректный ID записи.")
                    return
                keys = data[0].keys()
                new_entry = {}
                print("Введите новые значения: ")
                for key in keys:
                    if key == 'work_phone' or key == 'personal_phone':
                        new_entry[key] = validate_phone_number(key)
                    else:
                        new_entry[key] = input(f"{key} - ")

                data[entry_id - 1] = new_entry
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=2)
                file.truncate()
                print("Запись успешно отредактирована.")
                return ""
        except json.JSONDecodeError:
            print("В книге нет записей или они не корректны.")
            return ""

    def search_data(self):
        """ Поиск записей """
        try:
            with open(self.file_name, "r", encoding=self.encoding) as file:
                data = json.load(file)

                search_criteria = input("Введите критерии поиска: ").lower()
                found_entries = []

                for entry in data:
                    for value in entry.values():
                        if search_criteria in str(value).lower():
                            found_entries.append(entry)
                            break

                if found_entries:
                    print("Найденные записи:")
                    for found_entry in found_entries:
                        print(found_entry)
                else:
                    print("Записи по указанным критериям не найдены.")
                return ""
        except json.JSONDecodeError:
            print("В книге нет записей или они не корректны.")
            return ""


