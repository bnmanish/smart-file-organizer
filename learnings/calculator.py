# Enter first number: 20
# Enter second number: 10

# ===== Result =====
# Addition       : 30
# Subtraction    : 10
# Multiplication : 200
# Division       : 2.0
# ==================


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print('===== Result =====')
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print('==================')