# write a calculator program that has a menu system where it asks for a choice from user (+, -, *, /, !). it should display the output until the user explicitely terminates the program by writing exit.

while True:
    user_choice = input("Enter your choice (+, -, *, /, ! or exit): ")

    if user_choice == "exit":
        break

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    match user_choice:
        case '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        case '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Division by zero cannot be performed")
        case "!":
            if num1 < 0:
                print("Factorial is not defined for negative numbers")
            else:
                factorial = 1
                for i in range(1, num1 + 1):
                    factorial *= i
                print(f" factorial of {num1} is: {factorial}")
        case _:
            print("Invalid choice, please try again!")
        