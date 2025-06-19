operation = input("Enter operation (add, subtract, multiply, divide): ")
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

i = 0
if operation == "add":
    result = 0
    while i < len(numbers):
        result += numbers[i]
        i += 1

elif operation == "subtract":
    result = numbers[0]
    i = 1
    while i < len(numbers):
        result -= numbers[i]
        i += 1

elif operation == "multiply":
    result = 1
    while i < len(numbers):
        result *= numbers[i]
        i += 1

elif operation == "divide":
    try:
        result = numbers[0]
        i = 1
        while i < len(numbers):
            result /= numbers[i]
            i += 1
    except ZeroDivisionError:
        print("Error: Division by zero.")
        result = None

else:
    print("Invalid operation.")
    result = None

if result is not None:
    print("Result:", result)
