import logic


def ask():
    print('Calculator alkalmazás')

    print('1. operand  (integer)')
    text = input()
    while not logic.is_numeric(text):
        print('Bad input, please try again: (integer)')
        text = input()
    operand1 = int(text)

    print('operator (+, -, *, /)')
    text = input()
    while not logic.is_supported_operator(text):
        print('Bad input, please try again: (+, -, *, /)')
        text = input()
    operator = text

    print('2. operand (integer)')
    text = input()
    while not text.isnumeric():
        print('Bad input, please try again: (integer)')
        text = input()
    operand2 = int(text)

    return operand1, operator, operand2


def calculate(operand1, operator, operand2):
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    return result


op1, operator, op2 = ask()
result = logic.calculate(op1, operator, op2)
print(result)
exit(0)
