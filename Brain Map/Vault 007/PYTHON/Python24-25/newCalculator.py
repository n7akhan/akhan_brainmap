

answer = ""





while answer != "no":

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input(f"Choose an operator (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero! Try again!")
            continue
        result = num1 / num2
    else:
        print("Invalid operator, please chose again! (+, -, *, /)")
        continue
    print(f"The result is {result}")
    answer = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
print("Have a great day! ")

