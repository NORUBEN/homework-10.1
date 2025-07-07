from datetime import datetime
from typing import Dict, List
from collections import Counter
import re


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """ Фильтрует список банковских операций по значению ключа 'state' """
    filtered = []  # создаём пустой список для результата
    for operation in data:
        if operation.get("state") == state:
            filtered.append(operation)  # добавляем подходящую операцию
    return filtered  # возвращаем отфильтрованный список


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует список банковских операций по дате."""
    # Используем встроенную функцию sorted
    # Ключ сортировки — дата, преобразованная в объект datetime
    return sorted(data, key=lambda operation: datetime.fromisoformat(operation["date"]), reverse=reverse)

def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """ Возвращает список операций, содержащих строку search в описании (без учёта регистра)  """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """ Подсчитывает количество операций по категориям (по описанию). """
    descriptions = [item.get("description", "") for item in data]
    filtered = [desc for desc in descriptions if desc in categories]
    return dict(Counter(filtered))