"""
Question 3: Write a Python program to calculate the distance 
between two points (x1, y1) and (x2, y2).
"""
import math

# Step 1: Input coordinates for the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# math.sqrt is for square root, and **2 is for squaring
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("The distance between the two points is:", distance)
print("Data Type of result:", type(distance))