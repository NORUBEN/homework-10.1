import json
import logging
import os
from typing import Any, Dict, List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает список транзакций из JSON-файла"""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Успешно загружен JSON из {file_path}")
                return data
            logger.error(f"Формат данных в файле {file_path} не является списком")
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Ошибка при чтении файла {ex}")
    except Exception as ex:
        logger.error(f"Неизвестная ошибка {ex}")
    return []


if __name__ == "__main__":
    test_path = os.path.join(BASE_DIR, "data", "operations.json")
    transactions = load_transactions(test_path)
    print(f"Загружено {len(transactions)} транзакций")
