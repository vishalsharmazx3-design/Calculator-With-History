'''
This is also a mini project 
in this project i created a calculator with history feature.

In this calculator we made a features like history clear, exit

concepts we used in this project are:

1. Input (input() - To get the user's operation or
command

2.Functions - To organize code (calculating,
showing history, etc.)

3. Conditionals - To decide what to do: calculation,
history, or clear

4. File Handling - To save/load/clear history in
a .txt file

5. Loops (while) - To keep the program running
until user exits

6. Basic Math - For calculator
operations: +, -, *, /

Features : 
- Basic Calculator Operations
- History Tracking and save
- Clear History
- Exit Functionality
'''

# 1 - Define the name of the history file ( e.g "history.txt")



history_file = "history.txt"


def show_history():
    try:
        file = open(history_file, "r")
        lines = file.readlines()

        if len(lines) == 0:
            print("No history found.")
        else:
            for line in reversed(lines):
                print(line.strip())

        file.close()

    except FileNotFoundError:
        print("No history found.")


def clear_history():
    file = open(history_file, "w")
    file.close()
    print("History cleared.")


def save_to_history(equation, result):
    file = open(history_file, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculate(user_input):

    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Use format: 8 + 8")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return

        result = num1 / num2

    else:
        print("Invalid operator. Use only + - * /")
        return

    if int(result) == result:
        result = int(result)

    print("Result:", result)

    save_to_history(user_input, result)


def main():

    print("----- SIMPLE CALCULATOR -----")
    print("Type: history | clear | exit")

    while True:

        user_input = input("\nEnter calculation: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        elif user_input.lower() == "history":
            show_history()

        elif user_input.lower() == "clear":
            clear_history()

        else:
            calculate(user_input)


main()

