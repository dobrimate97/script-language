import sys

import logic


def print_usage_and_exit():
    print('calculator app. usage: OPERAND OPERATOR OPERAND. f.e. 3 + 5')
    exit(-1)


def get_inputs():
    if len(sys.argv) != 4:
        print_usage_and_exit()

    if not logic.is_numeric(sys.argv[1]):
        print_usage_and_exit()
    op1 = int(sys.argv[1])

    if not logic.is_numeric(sys.argv[2]):
        print_usage_and_exit()
    operator = sys.argv[2]

    if not logic.is_numeric(sys.argv[3]):
        print_usage_and_exit()
    op2 = int(sys.argv[3])
    return op1, operator, op2


operand1, operator, operand2 = get_inputs()
result = logic.calculate(operand1, operator, operand2)
print(result)
exit(0)
