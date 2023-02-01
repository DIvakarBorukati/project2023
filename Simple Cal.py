
print("Calculator")
print("Enter 'quit' to end the program")

while True:
    X = input("Enter a number (or 'quit'): ")
    if X == 'quit':
        break
    Y = input("Enter another number (or 'quit'): ")
    if Y == 'quit':
        break
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == '+':
        result = float(X) + float(Y)
    elif operation == '-':
        result = float(X) - float(Y)
    elif operation == '*':
        result = float(X) * float(Y)
    elif operation == '/':
        result = float(X) / float(Y)
    else:
        print("Unknown operation")
        continue

    print("Result:", result)


