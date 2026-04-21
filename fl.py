<<<<<<< HEAD
# Writing to a file
f = open("sample.txt", "w")
f.write("Hello, File!\n")
f.write("Second line\n")
f.writelines(["Third line\n", "Fourth line\n"])
f.close()
# Reading a file
f = open("sample.txt", "r")
print(f.read()) # Read entire file
f.close()
f = open("sample.txt", "r")
print(f.readline()) # Read one line
f.close()
f = open("sample.txt", "r")
print(f.readlines()) # Read all lines as list
f.close()
# Best practice: using 'with' statement (context manager)
with open("sample.txt", "r") as f:
for line in f:
print(line.strip()) # Read line by line
# Appending to a file
with open("sample.txt", "a") as f:
f.write("Appended line\n")
# Count words in a file
with open("sample.txt", "r") as f:
content = f.read()
words = content.split()
print("Word count:", len(words))
# Copy file content
with open("sample.txt", "r") as src:
with open("copy.txt", "w") as dst:
dst.write(src.read())
=======
# File name: fl1.py
# Program to open and read a file

# -------------------------------
# Section 1: Read entire file
# -------------------------------

# Open the file in read mode ("r")
# r before the path makes it a raw string (avoids escape sequence issues)
f = open(r"C:\Users\blk3-308\hmpmanish.txt", "r")

# Read the entire content of the file and print it
print(f.read())

# Close the file after reading
f.close()


# -------------------------------
# Section 2: Read only the first line
# -------------------------------

# WAP (Write a Program) to open and read a file (one line)

# Open the file in read mode ("r")
# r before the path is a raw string to avoid escape sequence errors
f = open(r"C:\Users\blk3-308\hmpmanish.txt", "r")

# Read only the first line from the file
print(f.readline())

# Close the file after reading
f.close()


# -------------------------------
# Section 3: Write data into a file
# -------------------------------

# WAP (Write a Program) to open a file and write data into it

# Open the file in write mode ("w")
# If the file does not exist, it will be created
# If it exists, its previous content will be erased
f = open(r"C:\Users\blk3-308\hmpmanish1.txt", "w")

# Write data into the file
# write() returns the number of characters written
print(f.write("Hello Manish 2"))

# Close the file after writing
f.close()


# -------------------------------
# Section 4: Write a list to a file, then read from another file
# -------------------------------

# WAP (Write a Program) to open a file and write a list, then read from another file

# Open file 'hmpmanish.txt' in write mode ("w")
# If the file does not exist, it will be created
f = open(r"C:\Users\blk3-308\hmpmanish.txt" ,"w")

# Create a list of names
L = ["Manish", "yash", "vikky", "swastik", "naman"]

# Write the list to the file
# Note: writelines() writes items as-is, without adding newlines
(f.writelines(L))

# Close the file after writing
f.close()

# Open another file 'hmpmanish1.txt' in read mode ("r")
# This file must exist, otherwise it will cause FileNotFoundError
f = open(r"C:\Users\blk3-308\hmpmanish1.txt" ,"r")

# Read and print only the first line of the file
print(f.readline())
>>>>>>> f82da6ee4030a47e4b695c9c1dcfe1a4c068c6e3
