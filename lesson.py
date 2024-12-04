lombada = input("Что соизволите исполнить: ")

a = float(input("1 число: "))
b = float(input("2 число: "))

if lombada == "+":
    c = a + b
    print(c)
elif lombada == "-":
    c = a - b
    print(c)
elif lombada == "*":
    c = a * b
    print(c)
elif lombada == "/":
    c = a / b
    print(c)
else:
    print("Ошибочка")


# 2
students = [
    {"n": "bobik", "ag": 40},
    {"n": "mobik", "ag": 40},
    {"n": "fobik", "ag": 167},
    {"n": "dodik", "ag": 166},
    {"n": "KRoLik", "ag": 40},
]
result = {}
for student in students:
    if student["ag"] not in result:
        result[student["ag"]] = []
    result[student["ag"]].append(student["n"])
print(result)
# name = n
# age = ag


# 3
# Я вообще не могу вдюплить как это выполнить 😖
def encrypt(text, shift):
    result = ""
    for char in text
# # «Попробуйте еще раз. Облажайтесь снова. Облажайтесь лучше».
# # Сэмюэл Беккет,писатель.
# # 4
def analyze_expenses(expenses):
    total = sum(exp["a"] for exp in expenses)
    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["a"]
    return f"Total: {total}, Max category: {max(categories, key=categories.get)}"


expenses = [
    {"category": "clothing", "a": 250.5},
    {"category": "travel", "a": 180.3},
    {"category": "clothing", "a": 90.7},
    {"category": "education", "a": 300},
    {"category": "travel", "a": 120.2},
]
print(analyze_expenses(expenses))