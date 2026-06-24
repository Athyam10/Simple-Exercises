import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

print(f"First argument: {arg1}")
print(f"Second argument: {arg2}")
print(f"Third argument: {arg3}")

opr1 = int(arg1)
opr2 = (arg2)
opr3 = int(arg3)

if opr2 == '+':
    result = opr1 + opr3
    print(f"The result of {opr1} {opr2} {opr3} is: {result}")
elif opr2 == '-':
    result = opr1 - opr3
    print(f"The result of {opr1} {opr2} {opr3} is: {result}")
elif opr2 == '*':
    result = opr1 * opr3
    print(f"The result of {opr1} {opr2} {opr3} is: {result}")
elif opr2 == '/':
    if opr3 != 0:
        result = opr1 / opr3
        print(f"The result of {opr1} {opr2} {opr3} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif opr2 == '%':
    if opr3 != 0:
        result = opr1 % opr3
        print(f"The result of {opr1} {opr2} {opr3} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use one of the following: +, -, *, /, %.")

