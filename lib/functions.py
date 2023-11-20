#!/usr/bin/env python3

# greet_programmer.py
def greet_programmer():
    print("Hello, programmer!")

# Redirect standard output to capture the printed message
import sys
from io import StringIO

original_stdout = sys.stdout
sys.stdout = StringIO()


greet_programmer()


printed_message = sys.stdout.getvalue().strip()


sys.stdout = original_stdout


assert printed_message == "Hello, programmer!", f"Expected 'Hello, programmer!', but got '{printed_message}'"



def greet(name):
    print(f"Hello, {name}!")

# Redirect standard output to capture the printed message
sys.stdout = StringIO()


greet("Guido")

# Get the printed message
printed_message = sys.stdout.getvalue().strip()


sys.stdout = original_stdout

# Assert that the printed message is equal to the expected string
assert printed_message == "Hello, Guido!", f"Expected 'Hello, Guido!', but got '{printed_message}'"



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Redirect standard output to capture the printed message
sys.stdout = StringIO()


greet_with_default()

# Get the printed message
printed_message = sys.stdout.getvalue().strip()

# Reset standard output
sys.stdout = original_stdout

# Assert that the printed message is equal to the expected string
assert printed_message == "Hello, programmer!", f"Expected 'Hello, programmer!', but got '{printed_message}'"

# Call the function with a custom name
sys.stdout = StringIO()
greet_with_default("Guido")
printed_message_custom = sys.stdout.getvalue().strip()
sys.stdout = original_stdout

# Assert that the printed message with a custom name is equal to the expected string
assert printed_message_custom == "Hello, Guido!", f"Expected 'Hello, Guido!', but got '{printed_message_custom}'"


# add.py
def add(num1, num2):
    return num1 + num2

# Call the function and assert the result
result = add(45, 55)
assert result == 100, f"Expected 100, but got {result}"


# halve.py
def halve(number):
    return number / 2

# Call the function and assert the result for an integer input
result_integer = halve(100)
assert result_integer == 50, f"Expected 50, but got {result_integer}"

# Call the function and assert the result for a float input
result_float = halve(99.0)
assert result_float == 49.5, f"Expected 49.5, but got {result_float}"
