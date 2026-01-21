"""
Question: Write a Python program that accepts two numbers from the user and 
prints their sum, difference, product, quotient, remainder and also 
print the datatype of each result.
"""

# Experiment-1: Basic Arithmetic
# Input two numbers from keyboard
a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))

# Calculations
sum_val = a + b
diff = a - b
prod = a * b
quotient = a / b
remainder = a % b

# Displaying results and data types
print("Sum =", sum_val, type(sum_val))
print("Difference =", diff, type(diff))
print("Product =", prod, type(prod))
print("Quotient =", quotient, type(quotient))
print("Remainder =", remainder, type(remainder))