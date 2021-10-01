import sys

import logic


def print_usage_and_exit():
    print('calculator app. usage: OPERAND OPERATOR OPERAND. f.e. 3 + 5')
    exit(-1)


def process_onerow(row):
    parts = row.split()
    if len(parts) != 3:
        print_usage_and_exit()

    if not logic.is_numeric(parts[0]):
        print_usage_and_exit()
    op1 = int(parts[0])

    if not logic.is_numeric(parts[1]):
        print_usage_and_exit()
    operator = parts[1]

    if not logic.is_numeric(parts[2]):
        print_usage_and_exit()
    op2 = int(parts[2])

    return op1, operator, op2


def get_inputs():
    for row in sys.stdin:
        operand1, operator, operand2 = process_onerow(row)
        result = logic.calculate(operand1, operator, operand2)
        print(result)


get_inputs()
exit(0)
