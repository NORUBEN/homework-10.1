import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: Dict) -> float:
    """Конвертирует сумму транзакции в рубли, используя внешний API"""
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")
    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        raise ValueError(f"Неподдерживаемая валюта: {currency}")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    rate = float(response.json()["rates"]["RUB"])
    return round(amount * rate, 2)
