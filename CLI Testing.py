import argparse

def simple_addition():
    parser = argparse.ArgumentParser(description = "Simple Addition Program to Test CLI")

    # each line add AN argument to our terminal inout
    parser.add_argument("first_number", type = int, help = "enter the first integer")
    parser.add_argument("second_number", type = int, help = "enter the second integer")
    args = parser.parse_args()

    # storing the entered argument internally within our code for ease of access
    first = args.first_number
    second = args.second_number

    # calculate and return the sum
    sum = first + second
    return sum

if __name__ == "__main__":
    print("The sum is: ", simple_addition())