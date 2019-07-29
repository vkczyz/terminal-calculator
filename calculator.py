#!/usr/bin/env python

import sys
import shelve

import operators as op

def to_float(number):
    """Converts numbers and variables to floats."""
    if number.isalpha():
        try:
            return float(shelf_file[number])
        except KeyError:
            print(f"'ERROR: Variable '{number}' does not exist")
            sys.exit()
    else:
        return float(number)


shelf_file = shelve.open('variables')

# Checks that the function and operand variables have been provided.
if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]
# Converts provided arguments into floats.
operands = [to_float(arg) for arg in sys.argv[2:]]

# Establishes valid keywords for performing an operation.
addition_commands = ['sum', 'add', 'addition', 'plus', '+']
subtraction_commands = ['difference', 'subtract', 'subtraction', 'minus', '-']
multiplication_commands = ['product', 'multiply', 'multiplication', '*']
division_commands = ['quotient', 'divide', 'division', '/']

# Calculates the answer using the correct function.
if function in addition_commands:
    answer = op.sum_(operands)
elif function in subtraction_commands:
    answer = op.difference(operands)
elif function in multiplication_commands:
    answer = op.product(operands)
elif function in division_commands:
    answer = op.quotient(operands)
else:
    print(f"ERROR: Command '{function}' not recognised")
    sys.exit()

# Assigns value to a given variable.
elif function == 'assign':
    variable = sys.argv[2].lower()
    value = to_float(sys.argv[3])
    if variable.isalpha() and len(variable) == 1:
        shelf_file[variable] = value
        print(f"'{variable}' is set to {value}")
    else:
        print(f"ERROR: '{variable}' is not a valid variable name")
        print('Values can only be assigned to single letters')
    shelf_file.close()
    sys.exit()

# Converts answer to integer, if applicable.
if answer.is_integer():
    answer = int(answer)
print(answer)

shelf_file['ans'] = answer
shelf_file.close()