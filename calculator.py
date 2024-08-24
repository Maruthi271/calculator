def calculator():
    print("Welcome to the simple calculator!")

    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))

    # Display the operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for the operation choice
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        return

    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Run the calculator function
calculator()

