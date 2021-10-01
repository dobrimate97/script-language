def is_numeric(text):
    return text.isnumeric()


def is_supported_operator(text):
    return text in ['+', '-', '*', '/']


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
