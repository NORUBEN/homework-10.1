import json
from typing import Dict, List

from src.importers import (
    read_csv_transactions,
    read_excel_transactions,
    read_json_transactions,
)
from src.processing import (
    filter_by_state,
    process_bank_search,
    sort_by_date,
)


def filter_by_currency(data: List[Dict], currency_name: str) -> List[Dict]:
    """Фильтрует список операций по валюте: работает как с JSON, так и с CSV/XLSX"""
    result = []
    for item in data:
        # путь для JSON
        json_currency = item.get("operationAmount", {}).get("currency", {}).get("name", "")
        # путь для CSV/XLSX
        csv_xlsx_currency = item.get("currency_name", "")
        if (
            json_currency.lower() == currency_name.lower()
            or csv_xlsx_currency.lower() == currency_name.lower()
        ):
            result.append(item)
    return result


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = read_json_transactions("data/operations.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_csv_transactions("data/transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_excel_transactions("data/transactions_excel.xlsx")
    else:
        print("Программа: Неверный выбор. Завершение.")
        return

    # Запрос и проверка статуса
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = (
            input(
                "Программа: Введите статус, по которому необходимо выполнить фильтрацию. \n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                "Пользователь: "
            )
            .strip()
            .upper()
        )
        if status in valid_statuses:
            break
        print(f'Программа: Статус операции "{status}" недоступен.')

    transactions = filter_by_state(transactions, status)
    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    # Сортировка по дате
    if input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower() == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию? \nПользователь: ").strip().lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse)

    # Фильтрация по рублям
    if input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower() == "да":
        if choice == "1":
            rub_name = "руб."
        else:
            rub_name = "Ruble"
        transactions = filter_by_currency(transactions, rub_name)

    # Поиск по описанию
    if (
        input("Программа: Отфильтровать список транзакций по определенному слову \nв описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
        == "да"
    ):
        word = input("Пользователь: Введите слово для поиска: ").strip()
        transactions = process_bank_search(transactions, word)

    # Пустая выборка
    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Вывод результата
    print("Программа: Распечатываю итоговый список транзакций...\n")
    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}\n")

    for tx in transactions:
        date = tx.get("date", "")[:10]
        description = tx.get("description", "Без описания")
        from_acc = tx.get("from")
        to_acc = tx.get("to")
        amount = (
                tx.get("operationAmount", {}).get("amount")
                or tx.get("amount")
                or ""
        )
        currency = (
                tx.get("operationAmount", {}).get("currency", {}).get("name")
                or tx.get("currency_name")
                or ""
        )

        print(f"{date} {description}")
        if from_acc and to_acc:
            print(f"{from_acc} -> {to_acc}")
        elif to_acc:
            print(f"-> {to_acc}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
# фиктивный пуш feature/re-collections-random
