import pytest

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def fail(a: int, b: int) -> float:
    return a / b


def test_log_success(capsys):
    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert "add error" not in captured.out


def test_log_error(capsys):
    with pytest.raises(ZeroDivisionError):
        fail(1, 0)
    captured = capsys.readouterr()
    assert "fail error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_file(tmp_path):
    log_path = tmp_path / "log.txt"

    @log(filename=str(log_path))
    def multiplay(x: int, y: int) -> int:
        return x * y

    result = multiplay(4, 5)
    assert result == 20

    content = log_path.read_text(encoding="utf-8")
    assert "multiplay ok" in content
