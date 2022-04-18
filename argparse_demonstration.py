"""
Description:
    1. This file demonstrate how to use argparse to write Python programs that takes input from the terminal.

Command Line Structure:
    python3 argparse_demonstration.py <first number> <second number>

Command Line Example:
    python3 argparse_demonstration.py 3 4
"""

import argparse

# this line creates an object of class argparse.ArgumentParser that will handle our terminal input
parser = argparse.ArgumentParser(description = "Demonstrating Argparse Library")

# each line add AN argument to our terminal inout
parser.add_argument("first_number", type = int, help = "enter the first integer")
parser.add_argument("second_number", type = int, help = "enter the second integer")

# this line parse all created arguments into a variable, so we can then call this variable to access the values of
# each argument within our args object
args = parser.parse_args()

# storing the entered argument internally within our code for ease of access
first = args.first_number
second = args.second_number

# find the sum (random basic operation)
sum = first + second

# print out the sum
print("The sum of", first, "and", second, "is", sum, "and no less.")