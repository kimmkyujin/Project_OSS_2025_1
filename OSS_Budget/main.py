from budget import Budget

def get_recommended_calories(weight_kg):
    """하루 권장 섭취 칼로리 계산"""
    return weight_kg * 30

def main():
    # 몸무게 입력
    while True:
        try:
            weight = float(input("몸무게를 입력하세요: "))
            if weight <= 0:
                print("0보다 큰 값을 입력해주세요.\n")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다.\n")
    
    recommended_cal = get_recommended_calories(weight)
    print(f"\n[안내] 하루 권장 섭취 칼로리: {recommended_cal}kcal\n")
    
    budget = Budget(recommended_cal)  
    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
