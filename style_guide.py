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
print("Hello, world!") 

# 3. Line Length 
# Correct:
def long_function_name(
    arg1, arg2, arg3, arg4
):
    return arg1 + arg2 + arg3 + arg4

# Wrong:
def long_function_name(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8  

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
import os, sys 

# 6. Docstrings
# Correct:
def add(a, b):
    return a + b

# Wrong:
def add(a, b):
    return a + b
