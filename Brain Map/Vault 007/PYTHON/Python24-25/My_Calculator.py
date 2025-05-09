import math
#
#This is a simple calculator program!
#In the future maybe use recurrision?
#Program will take in operator and then perform arethmitic operations on it!

operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    result = num1 + num2
    print(round(result,2))
elif operator == "-":
    result = num1 - num2
    print(round(result,2))
elif operator == "*":
    result = num1 * num2
    print(round(result,2))
elif operator == "/":
    result = num1 / num2
    print(round(result,2))
else:
    print("Please use a correct opperator!")
