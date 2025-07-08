from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует строку с номером карты или счёта.
    Если строка начинается с 'Счет', применяется маскирование счёта.
    В остальных случаях — карты.
    """
    parts = data.split()
    if parts[0] == "Счет":
        return f"Счет {get_mask_account(parts[1])}"
    else:
        card_type = " ".join(parts[:-1])
        card_number = parts[-1]
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407'
    в формат 'ДД.ММ.ГГГГ'
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
