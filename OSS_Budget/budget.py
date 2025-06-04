import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        calories = None
        if category == "식비":
            try:
                calories = int(input("칼로리(kcal): "))
            except ValueError:
                print("잘못된 칼로리입니다. 지출이 추가되지 않습니다.\n")
                return  # 잘못 입력하면 아예 추가하지 않음
        expense = Expense(today, category, description, amount, calories)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def total_calories_today(self):
        today = datetime.date.today().isoformat()
        total_cal = sum(
            e.calories for e in self.expenses
            if e.category == "식비" and e.date == today and e.calories is not None
        )
        print(f"오늘 섭취한 총 칼로리: {total_cal}kcal\n")
