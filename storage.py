import json
import os

from expense import Expense

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")


def ensure_data_dir():
    """Создаёт директорию data/, если её нет."""
    os.makedirs(DATA_DIR, exist_ok=True)


def save_expenses(expenses):
    """Сохраняет список расходов в JSON-файл."""
    ensure_data_dir()
    data = [exp.to_dict() for exp in expenses]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_expenses():
    """Загружает список расходов из JSON-файла."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Expense.from_dict(item) for item in data]
