def def calculator ():
    print("=== Aminu Bashir's Calculator ===")

    while True:
        try:
            first = float(input("Enter first number: "))
            operation = input("Choose (+, -, *, /): ")
            second = float(input("Enter second number: "))

            if operation == "+":
                result = first + second
            elif operation == "-":
                result = first - second
            elif operation == "*":
                result = first * second
            elif operation == "/":
                if second == 0:
                    print("Cannot divide by zero.")
                    continue
                result = first / second
            else:
                print("Invalid operation.")
                continue

            print("Result:", result)

            again = input("Do another calculation? (yes/no): ").lower()
            if again != "yes":
                break

        except ValueError:
            print("Please enter valid numbers.")

calculator()
