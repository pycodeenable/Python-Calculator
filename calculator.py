x = float(input('Number One: '))
y = float(input('Number Two: '))
operation = input('Operation: ')
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Error')

if result is not None:
    print('Result: ', result)