# Functions
# Remember to add colon (:) to end of def line

def multiply(a, b):
    answer = a * b
    print(answer)

multiply(2, 3)
multiply(8, 3)
multiply(6, 2)
multiply(9, 5)
multiply(1320, 94881)

def say_hello(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

say_hello("Farhana", "Jamil")

def your_budget_is(income, expense1, expense2, expense3):
    budget = income - (expense1 + expense2 + expense3)
    print(expense1)
    print(expense2)
    print(expense3)
    print(f"Your budget is: {budget}")

your_budget_is(10000, 30, 1500, 300)

def format_name(first_name, last_name):
    name = first_name.capitalize() + last_name.capitalize()
    print(f"Hello! {name}")

format_name("sTEvEn ", "sUZUki")
