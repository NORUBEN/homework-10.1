import json
from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict]:
    """Считывает транзакции из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel_transactions(file_path: str) -> List[Dict]:
    """Считывает транзакции из Excel-файла."""
    df = pd.read_excel(file_path, engine="openpyxl")
    return df.to_dict(orient="records")


def read_json_transactions(file_path: str) -> List[Dict]:
    """Считывает транзакции из JSON-файла."""
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)
