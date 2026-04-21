"""You are provided with a list of grocery items purchased by a 
customer. As shown below. Write python code to print the name of 
the item and its quantity (occurrences in the list).
L=[“pen”,“ball”,“eraser”,“pen”,“band”,“pen”,“Pencil”,“ball”]
Which item is the most occurring item from the list? """



# Given list
L = ["pen", "ball", "eraser", "pen", "band", "pen", "Pencil", "ball"]

# Dictionary to store item counts
item_count = {}

# Count occurrences
for item in L:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1

# Print item names and their quantities
print("Item and their quantities:")
for item, count in item_count.items():
    print(item, ":", count)

# Find most occurring item
most_item = max(item_count, key=item_count.get)
print("\nMost occurring item:", most_item)
