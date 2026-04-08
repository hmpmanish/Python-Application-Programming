# Program to open and read a file

# Open the file in read mode ("r")
# r before the path makes it a raw string (avoids escape sequence issues)
f = open(r"C:\Users\blk3-308\hmpmanish.txt", "r")

# Read the entire content of the file and print it
print(f.read())

# Close the file after reading
f.close()
