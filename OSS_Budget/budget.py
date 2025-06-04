import datetime
from expense import Expense

class Budget:
    def __init__(self, recommended_calories):
        self.expenses = []
        self.recommended_calories = recommended_calories  # 권장 칼로리 저장

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        calories = None
        
        # 식비일 때만 칼로리 입력 
        if category == "식비":
            try:
                calories = int(input("칼로리(kcal): "))
            except ValueError:
                print("잘못된 칼로리입니다. 지출이 추가되지 않습니다.\n")
                return
        
        expense = Expense(today, category, description, amount, calories)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

        # 식비인 경우 칼로리 체크
        if category == "식비":
            today_total_cal = sum(
                e.calories for e in self.expenses
                if e.date == today and e.category == "식비" and e.calories is not None
            )
            if today_total_cal > self.recommended_calories:
                print("!!과식했습니다!!\n")

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
