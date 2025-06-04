class Expense:
    def __init__(self, date, category, description, amount, calories=None):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.calories = calories  # 식비일 때만 사용

    def __str__(self):
        # 식비면 칼로리도 표시, 아니면 금액만 표시
        if self.category == "식비" and self.calories is not None:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원, {self.calories}kcal"
        else:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
