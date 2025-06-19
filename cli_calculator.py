def calculate(x, y, operation):
    if operation == 'add':
        return f"Result: {x + y}"
    
    elif operation == 'subtract':
        return f"Result: {x - y}"
    
    elif operation == 'multiply':
        return f"Result: {x * y}"
    
    elif operation == 'divide':
        if y == 0:
            return "Error: division by zero"
        return f"Result: {x / y}"
  

operation = input("Enter operation (add, subtract, multiply, divide): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

result = calculate(x, y, operation)
print(result)





        


