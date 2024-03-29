# Телефонная книга

Программа представляет собой простую телефонную книгу, которая позволяет пользователю просматривать, добавлять, редактировать и искать записи.

## Файлы

main.py - файл, содержащий логику консольного интерфейса для взаимодействия с телефонной книгой.

phonebook.py - файл, содержащий класс PhoneBook с методами для управления данными телефонной книги

service.py - файл, содержащий вспомогательные функции

data.json - файл с данными

## Функциональность

### 1. Просмотреть записи

Позволяет пользователю просматривать записи из телефонной книги постранично.

### 2. Добавить запись

Позволяет пользователю добавить новую запись в телефонную книгу. При добавлении новой записи программа проверяет корректность введенных данных, особенно номеров телефонов.

### 3. Редактировать запись

Позволяет пользователю редактировать существующую запись в телефонной книге. Пользователь может выбрать запись по ее номеру и изменить соответствующие значения.

### 4. Поиск записей

Позволяет пользователю выполнить поиск записей в телефонной книге по заданному критерию. Программа выводит все записи, в которых найдено совпадение.

### 5. Выйти

Позволяет пользователю выйти из программы.

## Как использовать

1. Запустите программу.
2. Следуйте инструкциям в меню для выполнения нужного действия.

## Используемые технологии

- Python 3
- JSON (для хранения данных)

## Зависимости

Отсутствуют. Программа использует стандартную библиотеку Python.