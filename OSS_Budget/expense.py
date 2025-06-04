class Expense:
    def __init__(self, date, category, description, amount, calories=None):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.calories = calories  

    def __str__(self):
        if self.category == "식비" and self.calories is not None:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원, {self.calories}kcal"
        else:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
