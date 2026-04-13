from datetime import datetime


CATEGORIES = [
    "Еда",
    "Транспорт",
    "Развлечения",
    "Здоровье",
    "Одежда",
    "Образование",
    "Другое",
]


class Expense:
    """Один расход."""

    def __init__(self, amount, category, description="", date=None, expense_id=None):
        self.id = expense_id or self._generate_id()
        self.amount = self._validate_amount(amount)
        self.category = self._validate_category(category)
        self.description = description.strip()
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def _validate_amount(amount):
        try:
            value = float(amount)
        except (TypeError, ValueError):
            raise ValueError(f"Сумма должна быть числом, получено: {amount}")
        if value <= 0:
            raise ValueError(f"Сумма должна быть положительной, получено: {value}")
        return round(value, 2)

    @staticmethod
    def _validate_category(category):
        if category not in CATEGORIES:
            raise ValueError(
                f"Неизвестная категория: '{category}'. "
                f"Доступные: {', '.join(CATEGORIES)}"
            )
        return category

    @staticmethod
    def _generate_id():
        return datetime.now().strftime("%Y%m%d%H%M%S%f")

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data.get("description", ""),
            date=data.get("date"),
            expense_id=data.get("id"),
        )

    def __str__(self):
        return f"[{self.date}] {self.category}: {self.amount:.2f} руб. — {self.description}"


class ExpenseTracker:
    """Менеджер расходов: добавление, удаление, поиск."""

    def __init__(self):
        self.expenses = []

    def add(self, amount, category, description=""):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        return expense

    def remove(self, expense_id):
        for i, exp in enumerate(self.expenses):
            if exp.id == expense_id:
                return self.expenses.pop(i)
        return None

    def get_all(self):
        return sorted(self.expenses, key=lambda e: e.date, reverse=True)

    def find_by_category(self, category):
        return [e for e in self.expenses if e.category == category]

    def count(self):
        return len(self.expenses)
