"""
Question: Write a Python program to check whether a number entered 
by the user is Even Or Odd.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even number.")
    print("Data Type:", type(num))
else:
    print(num, "is an Odd number.")
    print("Data Type:", type(num))