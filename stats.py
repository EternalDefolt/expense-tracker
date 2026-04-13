from collections import defaultdict

from expense import CATEGORIES


def total_sum(expenses):
    """Общая сумма всех расходов."""
    return sum(exp.amount for exp in expenses)


def sum_by_category(expenses):
    """Суммы расходов по категориям."""
    result = defaultdict(float)
    for exp in expenses:
        result[exp.category] += exp.amount
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


def sum_by_month(expenses):
    """Суммы расходов по месяцам (YYYY-MM)."""
    result = defaultdict(float)
    for exp in expenses:
        month_key = exp.date[:7]  # "2024-03" из "2024-03-15"
        result[month_key] += exp.amount
    return dict(sorted(result.items()))


def top_expenses(expenses, limit=5):
    """Самые крупные расходы."""
    return sorted(expenses, key=lambda e: e.amount, reverse=True)[:limit]


def print_stats(expenses):
    """Выводит полную статистику в консоль."""
    if not expenses:
        print("\n  Расходов пока нет.")
        return

    print(f"\n  Всего расходов: {len(expenses)}")
    print(f"  Общая сумма: {total_sum(expenses):.2f} руб.")

    print("\n  --- По категориям ---")
    for cat, amount in sum_by_category(expenses).items():
        print(f"  {cat:<15} {amount:>10.2f} руб.")

    print("\n  --- По месяцам ---")
    for month, amount in sum_by_month(expenses).items():
        print(f"  {month:<15} {amount:>10.2f} руб.")

    top = top_expenses(expenses, 3)
    if top:
        print("\n  --- Топ-3 расхода ---")
        for i, exp in enumerate(top, 1):
            print(f"  {i}. {exp}")
