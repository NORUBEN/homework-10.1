from pathlib import Path

from src.utils import load_transactions


def test_load_valid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "valid.json"
    file_path.write_text('[{"amount": 100, "currency": "USD"}]', encoding="utf-8")
    result = load_transactions(str(file_path))
    assert isinstance(result, list)
    assert result[0]["amount"] == 100


def test_load_invalid_json(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{bad json]", encoding="utf-8")
    result = load_transactions(str(file_path))
    assert result == []


def test_file_not_found() -> None:
    result = load_transactions("nonexistent.json")
    assert result == []
