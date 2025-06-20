from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict]:
    """Считывает транзакции из CSV-файла."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel_transactions(file_path: str) -> List[Dict]:
    """Считывает транзакции из Excel-файла."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
