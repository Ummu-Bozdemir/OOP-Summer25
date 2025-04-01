# 1. Naming Conventions
# Correct:
def calculate_total(price, tax):
    return price + tax

# Wrong:
def CALCULATE_TOTAL(PRICE, TAX):
    return PRICE + TAX

# 2. Indentation
# Correct:
def say_hello():
    print("Hello, world!")

# Wrong:
def say_hello():
print("Hello, world!")  # Incorrect indentation

# 3. Line Length (Max 79 characters)
# Correct:
def long_function_name(
    arg1, arg2, arg3, arg4
):
    return arg1 + arg2 + arg3 + arg4

# Wrong:
def long_function_name(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8  # Too long

# 4. Whitespace Usage
# Correct:
x = (1, 2, 3)
y = x[1]

# Wrong:
x=( 1,2, 3 )
y =x [ 1 ]

# 5. Import Statements
# Correct:
import os
import sys

# Wrong:
import os, sys  # Multiple imports in one line

# 6. Docstrings
# Correct:
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# Wrong:
def add(a, b):
    # This function adds two numbers
    return a + b
