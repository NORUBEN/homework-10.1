from typing import List, Dict
from datetime import datetime


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список банковских операций по значению ключа 'state'
    """
    filtered = []  # создаём пустой список для результата
    for operation in data:
        if operation.get("state") == state:
            filtered.append(operation)  # добавляем подходящую операцию
    return filtered  # возвращаем отфильтрованный список


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список банковских операций по дате.
    """
    # Используем встроенную функцию sorted
    # Ключ сортировки — дата, преобразованная в объект datetime
    return sorted(
        data,
        key=lambda operation: datetime.fromisoformat(operation["date"]),
        reverse=reverse
    )