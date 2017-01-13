operators = ['+', '-', '*', '/']


try:
    x = float(input('Enter first number: '))
    operator = input('Enter operation, that you need: ')
    y = float(input('Enter second number: '))

    #print(x, operator, y)


    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('Division by zero is forbidden.')

    if operator in operators:
        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        elif operator == '/':
            result = division(x, y)
        print(result)
    else:
        print('You wrote wrong operator. Try again')
except ValueError:
    print('Something is wrong')
