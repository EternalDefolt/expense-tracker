from expense import ExpenseTracker, CATEGORIES
from storage import save_expenses, load_expenses
from stats import print_stats


def show_menu():
    print("\n" + "=" * 40)
    print("    УЧЁТ РАСХОДОВ")
    print("=" * 40)
    print("  1. Добавить расход")
    print("  2. Показать все расходы")
    print("  3. Удалить расход")
    print("  4. Статистика")
    print("  5. Выход")
    print("-" * 40)


def input_expense(tracker):
    """Диалог добавления нового расхода."""
    print("\n  Категории:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    try:
        cat_num = int(input("\n  Номер категории: ")) - 1
        if cat_num < 0 or cat_num >= len(CATEGORIES):
            print("  Неверный номер категории!")
            return
        category = CATEGORIES[cat_num]
    except ValueError:
        print("  Введите число!")
        return

    try:
        amount = float(input("  Сумма (руб.): "))
    except ValueError:
        print("  Введите корректную сумму!")
        return

    description = input("  Описание (необязательно): ").strip()

    try:
        expense = tracker.add(amount, category, description)
        print(f"\n  Добавлено: {expense}")
    except ValueError as e:
        print(f"  Ошибка: {e}")


def show_expenses(tracker):
    """Показать все расходы."""
    expenses = tracker.get_all()
    if not expenses:
        print("\n  Расходов пока нет.")
        return

    print(f"\n  {'#':<4} {'Дата':<12} {'Категория':<15} {'Сумма':>10}  {'Описание'}")
    print("  " + "-" * 60)
    for i, exp in enumerate(expenses, 1):
        print(f"  {i:<4} {exp.date:<12} {exp.category:<15} {exp.amount:>10.2f}  {exp.description}")
    print(f"\n  Итого: {sum(e.amount for e in expenses):.2f} руб.")


def delete_expense(tracker):
    """Удалить расход по номеру."""
    expenses = tracker.get_all()
    if not expenses:
        print("\n  Нечего удалять.")
        return

    show_expenses(tracker)

    try:
        num = int(input("\n  Номер для удаления: ")) - 1
        if num < 0 or num >= len(expenses):
            print("  Неверный номер!")
            return
        removed = tracker.remove(expenses[num].id)
        if removed:
            print(f"  Удалено: {removed}")
    except ValueError:
        print("  Введите число!")


def main():
    tracker = ExpenseTracker()
    tracker.expenses = load_expenses()
    print(f"\n  Загружено расходов: {tracker.count()}")

    while True:
        show_menu()
        choice = input("  Выбор: ").strip()

        if choice == "1":
            input_expense(tracker)
            save_expenses(tracker.expenses)
        elif choice == "2":
            show_expenses(tracker)
        elif choice == "3":
            delete_expense(tracker)
            save_expenses(tracker.expenses)
        elif choice == "4":
            print_stats(tracker.expenses)
        elif choice == "5":
            save_expenses(tracker.expenses)
            print("\n  До встречи!\n")
            break
        else:
            print("  Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
