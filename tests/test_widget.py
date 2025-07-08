import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    result = mask_account_card(input_data)
    assert result == expected


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ],
)
def test_get_date(input_date: str, expected: str) -> None:
    result = get_date(input_date)
    assert result == expected
