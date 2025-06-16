import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "masks.log"), mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты, оставляя первые 6 и последние 4 цифры."""
    try:
        card_str = str(card_number)
        masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        logger.debug(f"Маскирование карты: {card_number} в {masked}")
        return masked
    except Exception as ex:
        logger.error(f"Ошибка маскирования карты: {ex}")
        return ""


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры с двумя звездочками."""
    try:
        account_str = str(account_number)
        masked = f"**{account_str[-4:]}"
        logger.debug(f"Маскирование счета: {account_number} в {masked}")
        return masked
    except Exception as ex:
        logger.error(f"Ошибка маскирования счета: {ex}")
        return ""


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345678"))
    print(get_mask_account("40817810099910004312"))
