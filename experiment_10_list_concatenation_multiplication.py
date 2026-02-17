"""Write a Python program to concatenate two lists and then perform 
element-wise multiplication of the resulting list by 3."""
#hmpmanish

# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate the lists
combined_list = list1 + list2

# Perform element-wise multiplication by 3
result = [element * 3 for element in combined_list]

# Display results
print("First List:", list1)
print("Second List:", list2)
print("Concatenated List:", combined_list)
print("After Multiplying by 3:", result)
