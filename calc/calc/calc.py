import random
import logging
import re

logging.getLogger().setLevel(logging.DEBUG)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

#TODO: 2. adding mul and div operators
#TODO: 3. add power function, handle operator priority
#TODO: 4. suppring float
OPERATORS = {
    "+": add,
    "-": sub,
}

def eval_var(var_name):
    if var_name == 'R':
        return random.randint(0, 10)
    elif var_name == 'G':
        return 9.81
    else:
        return ValueError('Variable %s not supported' % var_name)

def validate_eq(parsed_input):
    """Checks if equation is correct
    """
    #TODO: 1. check if every 2nd value is an operator
    pass

def parse_input(raw_input):
    """returns a array of eq elements
    2+5-R+3 -> ['2', '+', '5', '-', 'R', '+', '3']
    """
    split_input = re.split("([\+-])", raw_input.replace(' ', ''))
    if split_input:
        for i in range(len(split_input)):
            if split_input[i] in OPERATORS:
                # replace operator, with eval fn
                split_input[i] = OPERATORS[split_input[i]]
            elif split_input[i].isdigit():
                split_input[i] = int(split_input[i])
        return split_input
    raise ValueError("Invalid Input data %s" % raw_input)

def solve_eq(parsed_input):
    stack = []
    for el in parsed_input:
        if isinstance(el, str):
            el = eval_var(el)
        stack.append(el)
        if len(stack) >= 3:
            val_1, operator, val_2 = stack[0:3]
            stack[0] = operator(val_1, val_2)
            del stack[1:]

    assert len(stack) == 1
    return stack[0]

def calculate(raw_input):
    """Solves equation passed as raw_input, returns int value
    """
    parsed_input = parse_input(raw_input)
    validate_eq(parsed_input)
    return solve_eq(parsed_input)

if __name__ == "__main__":
    print(calculate("1+2-5+R"))
