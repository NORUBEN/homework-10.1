

# 🏦 Виджет банковских операций

## 📌 Цель проекта

Проект реализует backend-логику виджета, отображающего последние банковские операции клиента.

Виджет выполняет следующие задачи:
- Маскирует номера банковских карт и счетов
- Преобразует даты в удобочитаемый формат
- Фильтрует операции по статусу
- Сортирует операции по дате

---

## ⚙️ Установка

1. Установите [Poetry](https://python-poetry.org/docs/)
2. Установите зависимости:

```bash
poetry install
```

3. Запуск проекта:

```bash
poetry run python main.py
```

---

## 🧩 Структура проекта

```text
Homework_9.1/
├── src/
│   ├── generators.py        # Генераторы транзакций и номеров карт
│   ├── masks.py            # Маскировка номеров
│   ├── widget.py           # Преобразование строк и дат
│   └── processing.py       # Фильтрация и сортировка операций
├── tests/                  # Тесты
├── main.py                 # Точка входа
├── README.md               # Документация проекта
├── pyproject.toml          # Настройки Poetry и линтеров
├── poetry.lock             # Лок-файл Poetry
├── .flake8                 # Конфигурация Flake8
└── .gitignore              # Игнорируемые файлы
```

---

##  Реализованные функции

### `mask_account_card(data: str) -> str`

Маскирует номер карты или счёта из строки:

```python
from src.widget import mask_account_card

mask_account_card("Visa Platinum 7000792289606361")
# ➜ Visa Platinum 7000 79** **** 6361

mask_account_card("Счет 73654108430135874305")
# ➜ Счет **4305
```

---

### `get_date(date_str: str) -> str`

Преобразует дату из ISO-формата в `ДД.ММ.ГГГГ`:

```python
from src.widget import get_date

get_date("2024-03-11T02:26:18.671407")
# ➜ '11.03.2024'
```

---

### `get_mask_card_number(card_number: int) -> str`

Маскирует карту:  
Первые 6 и последние 4 цифры видны, остальные — звёздочки:

```python
from src.masks import get_mask_card_number

get_mask_card_number(7000792289606361)
# ➜ '7000 79** **** 6361'
```

---

### `get_mask_account(account_number: int) -> str`

Маскирует счёт:  
Видны только последние 4 цифры:

```python
from src.masks import get_mask_account

get_mask_account(73654108430135874305)
# ➜ '**4305'
```

---

### `filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]`

Фильтрует операции по ключу `state`.

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2024-05-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2023-03-01T08:00:00"}
]

filter_by_state(operations)
# ➜ [{'id': 1, 'state': 'EXECUTED', ...}]
```

---

### `sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]`

Сортирует операции по дате.

```python
from src.processing import sort_by_date

sort_by_date(operations)
# ➜ от новых к старым

sort_by_date(operations, reverse=False)
# ➜ от старых к новым
```

---

##  Проверка качества кода

Для проверки форматирования и типизации:

```bash
poetry run isort .
poetry run black .
poetry run flake8
poetry run mypy src/
```

---

## 👤 Автор

**GitHub:** [@NORUBEN](https://github.com/NORUBEN)

---

##  Пример входных данных

```python
operations = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364"
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441"
    }
]
```

## Тестирование

Для обеспечения стабильности и корректной работы проекта были написаны автоматические тесты с использованием библиотеки `pytest`.

### Как запустить тесты

1. Установите зависимости:
   ```
   poetry install
   ```

2. Запустите тесты:
   ```
   pytest --cov=src --cov-report=html
   ```

Отчёт о покрытии будет доступен в директории `htmlcov/index.html`.

### Покрытие

Проект покрыт тестами на **100%** (данные актуальны на момент последнего коммита). Покрываются все основные модули:
- `masks.py`
- `widget.py`
- `processing.py`
- `generators.py`

Используются:
- фикстуры (`@pytest.fixture`)
- параметризация (`@pytest.mark.parametrize`)
- аннотации типов (`mypy`)
- линтеры (`flake8`, `isort`)


## Модуль `generators`

Модуль `generators` предоставляет генераторы для работы с транзакциями и генерации номеров банковских карт.

---

### `filter_by_currency(transactions, currency)`

Фильтрует список транзакций по заданной валюте и возвращает итератор.

- **Аргументы:**
  - `transactions` — список словарей с транзакциями
  - `currency` — строка с кодом валюты (например, `"USD"`)

- **Возвращает:** генератор транзакций

**Пример:**
```python
from src.generators import filter_by_currency

for tx in filter_by_currency(transactions, "USD"):
    print(tx["id"], tx["operationAmount"]["amount"])
```

---

### `transaction_descriptions(transactions)`

Генератор, возвращающий описания операций из транзакций.

- **Аргументы:** список словарей
- **Возвращает:** генератор строк

**Пример:**
```python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

---

### `card_number_generator(start, stop)`

Генератор номеров карт в формате `XXXX XXXX XXXX XXXX`.

- **Аргументы:**
  - `start` — начальное значение (int)
  - `stop` — конечное значение (int)

- **Возвращает:** генератор строк

**Пример:**
```python
from src.generators import card_number_generator

for number in card_number_generator(1, 3):
    print(number)
```

**Вывод:**
```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```

