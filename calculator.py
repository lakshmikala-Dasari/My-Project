import logging

# --------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# CALCULATOR FUNCTIONS
# --------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# --------------------------------------------------
# DISPLAY HISTORY
# --------------------------------------------------

def show_history(history):

    if not history:
        print("\nNo operations performed yet.")
        return

    print("\n========== OPERATION HISTORY ==========")

    for operation in history:
        print(operation)

    print("========================================")

# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

history = []

print("===================================")
print("       ROBUST CALCULATOR")
print("===================================")

while True:

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show History")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    logging.info("User selected option: %s", choice)

    # ----------------------------------------------
    # SHOW HISTORY
    # ----------------------------------------------

    if choice == "5":
        show_history(history)
        continue

    # ----------------------------------------------
    # EXIT
    # ----------------------------------------------

    if choice == "6":
        print("\nThank you for using Robust Calculator!")
        logging.info("Calculator exited by user.")
        break

    # ----------------------------------------------
    # VALIDATE MENU CHOICE
    # ----------------------------------------------

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid choice! Please select 1-6.")
        logging.warning("Invalid menu choice: %s", choice)
        continue

    # ----------------------------------------------
    # GET NUMBERS
    # ----------------------------------------------

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        logging.info(
            "User entered numbers: %s and %s",
            num1,
            num2
        )

        # ------------------------------------------
        # PERFORM OPERATION
        # ------------------------------------------

        if choice == "1":

            result = add(num1, num2)
            symbol = "+"

        elif choice == "2":

            result = subtract(num1, num2)
            symbol = "-"

        elif choice == "3":

            result = multiply(num1, num2)
            symbol = "*"

        elif choice == "4":

            result = divide(num1, num2)
            symbol = "/"

        # ------------------------------------------
        # CREATE OPERATION RECORD
        # ------------------------------------------

        operation = f"{num1} {symbol} {num2} = {result}"

        history.append(operation)

        print("\nResult:", result)

        logging.info("Calculation successful: %s", operation)

    # ----------------------------------------------
    # INVALID NUMBER
    # ----------------------------------------------

    except ValueError:

        print("\nError: Please enter valid numbers.")

        logging.error(
            "Invalid numeric input entered by user."
        )

    # ----------------------------------------------
    # DIVISION BY ZERO
    # ----------------------------------------------

    except ZeroDivisionError as e:

        print("\nError:", e)

        logging.error(
            "Division by zero attempted."
        )

    # ----------------------------------------------
    # ALWAYS EXECUTED
    # ----------------------------------------------

    finally:

        logging.info("Calculation attempt completed.")