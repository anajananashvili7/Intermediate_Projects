def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        print("\nChoose an operation (1-4) or type 'exit' to quit.")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")

if __name__ == "__main__":
    calculator()
