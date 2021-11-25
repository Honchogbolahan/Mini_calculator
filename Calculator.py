print('SIMPLE CALCULATOR')
print("Note: Enter the numbers in the order of the operation to be performed")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose the operation to be performed: +, -, *, /")
select = input("Select operation: ")
if select == "*":
    print(num1, "*", num2, "=", num1*num2)
elif select == "+":
    print(num1, "+", num2, "=", num1+num2)
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)
else: print("Invalid Inputs")