import random
import logging
import re
import sys

logging.getLogger().setLevel(logging.DEBUG)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def power(x, y):
    return x ** y


OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "^": power,
}
OPERATORS_AT_THE_BEGINNING = ['add', 'sub']
HIGH_PRIORITY_OPERATORS = ['power']
MEDIUM_PRIORITY_OPERATORS = ['mul', 'div']


def eval_var(var_name):
    if var_name == 'R':
        return random.randint(0, 10)
    elif var_name == 'G':
        return 9.81
    else:
        raise ValueError('Variable %s not supported' % var_name)


def validate_eq(parsed_input):
    """Checks if equation is correct
    3+-5+RR -> ValueError
    """
    if not isinstance(parsed_input[0], float) \
       and not isinstance(parsed_input[0], str):

        if parsed_input[0].__name__ not in OPERATORS_AT_THE_BEGINNING:
            raise ValueError("Invalid operator %s at the beginning"
                             % parsed_input[0])

    elif not isinstance(parsed_input[len(parsed_input) - 1], float) \
            and not isinstance(parsed_input[len(parsed_input) - 1], str):

        raise ValueError("Invalid operator %s at the end"
                         % parsed_input[len(parsed_input) - 1])

    else:
        for i in range(1, len(parsed_input) - 1):
            if not isinstance(parsed_input[i], float) \
               and not isinstance(parsed_input[i], str):
                if (not isinstance(parsed_input[i - 1], float)
                    and not isinstance(parsed_input[i - 1], str)) \
                   or (not isinstance(parsed_input[i + 1], float)
                       and not isinstance(parsed_input[i + 1], str)):

                    raise ValueError("Invalid combination %s %s %s"
                                     % (parsed_input[i - 1], parsed_input[i],
                                        parsed_input[i + 1]))


def parse_input(raw_input):
    """returns a array of eq elements
    2+5-R+3 -> ['2', '+', '5', '-', 'R', '+', '3']
    """

    split_input = re.split("([\*^/\+-])", raw_input.replace(' ', ''))
    if isinstance(split_input, list) and split_input != ['']:
        split_input = [item for item in split_input if item != '']
        for i in range(len(split_input)):
            if split_input[i] in OPERATORS:
                split_input[i] = OPERATORS[split_input[i]]
            elif split_input[i].replace(".", "").isdigit():
                split_input[i] = float(split_input[i])
        return split_input
    raise ValueError("Invalid Input data %s" % raw_input)


def solve_eq(parsed_input):
    stack = []
    if not isinstance(parsed_input[0], float) \
       and not isinstance(parsed_input[0], str):

        operator = parsed_input[0]
        del parsed_input[0]
        parsed_input[0] = operator(0.0, parsed_input[0])

    for el in parsed_input:
        if isinstance(el, str):
            el = float(eval_var(el))
        stack.append(el)
    for i in range(len(parsed_input) - 1, 1, -1):
        if not isinstance(parsed_input[i], float) \
           and not isinstance(parsed_input[i], str):

            if parsed_input[i].__name__ in HIGH_PRIORITY_OPERATORS:
                val_1, operator, val_2 = stack[(i - 1):(i + 2)]
                stack[i - 1] = operator(val_1, val_2)
                del stack[i:(i + 2)]
    stack_len = len(stack)
    stack.reverse()
    for i in range(stack_len - 2, 0, -1):
        if not isinstance(stack[i], float) \
           and not isinstance(stack[i], str):
            if stack[i].__name__ in MEDIUM_PRIORITY_OPERATORS:
                val_2, operator, val_1 = stack[(i - 1):(i + 2)]
                stack[i - 1] = operator(val_1, val_2)
                del stack[i:(i + 2)]
    stack.reverse()
    new_stack = []
    for el in stack:
        new_stack.append(el)
        if len(new_stack) >= 3:
            val_1, operator, val_2 = new_stack[0:3]
            new_stack[0] = operator(val_1, val_2)
            del new_stack[1:]
    assert len(new_stack) == 1
    return new_stack[0]


def calculate(raw_input):
    """Solves equation passed as raw_input, returns float value
    """
    parsed_input = parse_input(raw_input)
    validate_eq(parsed_input)
    return solve_eq(parsed_input)


def main():
    """Main function
    """
    eq = sys.argv[1]
    print(calculate(eq))

if __name__ == "__main__":
    print(calculate("1.3+2*3-2^3-5/2+R"))
