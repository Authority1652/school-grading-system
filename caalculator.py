#  CALCULATOR PROJECT 
def calc():
        
    num1 = float(input("Enter a number: "))
    operator = input("Enter an arithemetic operator: (+ - / * ** % //): ")
    num2 = float(input("Enter a second number: "))

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {round(result, 2)}")

    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {round(result, 2)}")

    elif operator == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result, 2)}")

    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {round(result, 2)}")

    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {round(result, 2)}")

    elif operator == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {round(result, 2)}")
        
    elif operator == "//":
        result = num1 // num2
        print(f"{num1} // {num2} = {round(result, 2)}")
    else:
        print(f"{operator} is not a valid operator.")

calc()

while True:
    try_again = input("continue? enter(y/n): ").upper()
    if try_again == "n":
        print("Goodbye!!")
    else:
        break
    calc()


























# operator = input("Enter an arithemetic Operator (+, -, *, /, //, **, %): ")
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 2))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 2))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 2))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 2))
# elif operator == "//":
#     result = num1 // num2
#     print(round(result, 2))
# elif operator == "**":
#     result = num1 ** num2
#     print(round(result, 2))
# elif operator == "%":
#     result = num1 % num2
#     print(round(result, 2))
# else:
#     print(f"The operator you entered is invalid, please enter a valid operator")