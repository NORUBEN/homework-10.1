from unittest.mock import MagicMock, Mock, patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get: MagicMock) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 100.0}}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {"amount": 10, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result == 1000.0
    mock_get.assert_called_once()


def test_convert_rub() -> None:
    transaction = {"amount": 500, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 500.0
