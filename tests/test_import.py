from typing import Dict, List
from unittest.mock import patch

import pandas as pd
import pytest

from src.importers import read_csv_transactions, read_excel_transactions


@pytest.fixture
def fake_data() -> List[Dict[str, str | int]]:
    return [
        {"date": "2023-01-01", "amount": 100, "currency": "USD"},
        {"date": "2023-01-02", "amount": 200, "currency": "EUR"},
    ]


@patch("src.importers.pd.read_csv")
def test_read_csv_transactions(mock_read_csv, fake_data) -> None:
    df = pd.DataFrame(fake_data)
    mock_read_csv.return_value = df

    result = read_csv_transactions("dummy/path.csv")

    assert isinstance(result, list)
    assert result == fake_data
    mock_read_csv.assert_called_once_with("dummy/path.csv")


@patch("src.importers.pd.read_excel")
def test_read_excel_transactions(mock_read_excel, fake_data) -> None:
    df = pd.DataFrame(fake_data)
    mock_read_excel.return_value = df

    result = read_excel_transactions("dummy/path.xlsx")

    assert isinstance(result, list)
    assert result == fake_data
    mock_read_excel.assert_called_once_with("dummy/path.xlsx", engine="openpyxl")
