import sys
from phonebook import PhoneBook


def main():
    """Главная функция для работы с телефонной книгой."""
    phone_book = PhoneBook("data.json")

    actions = {
        "1": phone_book.display_data,
        "2": phone_book.add_data,
        "3": phone_book.change_entry,
        "4": phone_book.search_data,
        "5": lambda: sys.exit()
    }

    while True:
        print("Выберите действие:")
        print("1. Просмотреть записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
