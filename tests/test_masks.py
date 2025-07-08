import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (1234567812345678, "1234 56** **** 5678"),
        (1111222233334444, "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        (1234567890123456, "**3456"),
        (987654321, "**4321"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)
    assert result == expected
