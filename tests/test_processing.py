from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date
from src.processing import process_bank_search, process_bank_operations


@pytest.fixture()
def test_data() -> List[Dict[str, str]]:
    return [
        {"date": "2023-01-01T10:00:00", "state": "EXECUTED"},
        {"date": "2022-06-15T12:00:00", "state": "PENDING"},
        {"date": "2023-05-20T15:30:00", "state": "EXECUTED"},
        {"date": "2021-12-31T23:59:59", "state": "CANCELED"},
    ]


@pytest.mark.parametrize(
    "given_state, expected_amount", [("EXECUTED", 2), ("PENDING", 1), ("CANCELED", 1), ("UNKNOWN", 0)]
)
def test_filter_by_state(test_data: List[Dict[str, str]], given_state: str, expected_amount: int) -> None:
    result = filter_by_state(test_data, given_state)
    assert len(result) == expected_amount
    for r in result:
        assert r["state"] == given_state


def test_sort_by_date_reverse_true(test_data: List[Dict[str, str]]) -> None:
    sorted_list = sort_by_date(test_data, reverse=True)
    for i in range(len(sorted_list) - 1):
        assert sorted_list[i]["date"] >= sorted_list[i + 1]["date"]


def test_sort_by_date_reverse_false(test_data: List[Dict[str, str]]) -> None:
    sorted_list = sort_by_date(test_data, reverse=False)
    for i in range(len(sorted_list) - 1):
        assert sorted_list[i]["date"] <= sorted_list[i + 1]["date"]

transactions = [
    {"description": "Оплата мобильной связи"},
    {"description": "Покупка в магазине"},
    {"description": "Оплата ЖКХ"},
    {"description": "Подарок другу"},
]


def test_process_bank_search_found():
    result = process_bank_search(transactions, "оплата")
    assert len(result) == 2
    assert all("оплата" in item["description"].lower() for item in result)


def test_process_bank_search_not_found():
    result = process_bank_search(transactions, "налоги")
    assert result == []


def test_process_bank_operations_count():
    categories = ["Оплата ЖКХ", "Покупка в магазине"]
    result = process_bank_operations(transactions, categories)
    assert result == {"Оплата ЖКХ": 1, "Покупка в магазине": 1}


def test_process_bank_operations_empty():
    categories = ["Авто"]
    result = process_bank_operations(transactions, categories)
    assert result == {}