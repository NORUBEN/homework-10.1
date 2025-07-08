from typing import Dict, List


def filter_by_currency(transactions: List[Dict], currency: str):
    """Фильтрует транзакции по заданной валюте и возвращает итератор"""
    for transaction in transactions:
        currency_info = transaction.get("operationAmount", {}).get("currency", {})
        currency_code = currency_info.get("code")
        if currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]):
    """Генератор, возвращающий описания транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int):
    """Генератор номеров карт от start до stop включительно"""
    for number in range(start, stop + 1):
        card_number = f"{number:016}"
        formatted = " ".join(card_number[i:i + 4] for i in range(0, 16, 4))
        yield formatted

# временный комментарий