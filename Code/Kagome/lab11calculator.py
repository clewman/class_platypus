
while True:
    ans = input('What operation would you like to perform? select(+) for add, \nselect(-) for subtract, select(*) formultiple, or (/)for divide(/)')
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))

    if ans == '+':
        print(num1 + num2)
    if ans == '-':
        print(num1 - num2)
    if ans == '*':
        print(num1 * num2)
    if ans == '/':
        print(num1 / num2)

    continuecalc = input('Would you like to continue using the calculator? yes(y) or done(d)')


    if continuecalc == 'd':
        break







# def add(x, y):
#    return x + y
#
# def subtract(x, y):
#    return x - y
#
# def multiply(x, y):
#    return x * y
#
# def divide(x, y):
#    return x / y