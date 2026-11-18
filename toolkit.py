
# Personal Mini-Toolkit
# This program provides three useful tools.

# Tool 1: Simple Calculator
def calculator():
    print("\n--- Simple Calculator ---")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Choose an operation (1-4): ")

    if operation == "1":
        print(f"Result: {num1 + num2}")
    elif operation == "2":
        print(f"Result: {num1 - num2}")
    elif operation == "3":
        print(f"Result: {num1 * num2}")
    elif operation == "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Sorry, division by zero is not allowed.")
    else:
        print("Invalid operation.")


# Tool 2: To-Do List
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    number = int(input("Enter task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Tool 3: Even or Odd Checker
def even_odd_checker():
    print("\n--- Even or Odd Checker ---")

    try:
        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: keeps running until the user chooses Quit.
print("================================")
print("Welcome to My Personal Mini-Toolkit!")
print("================================")

while True:
    print("\nMAIN MENU")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Even or Odd Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        even_odd_checker()

    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 4.")
