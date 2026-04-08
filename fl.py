# Program to open and read a file

# Open the file in read mode ("r")
# r before the path makes it a raw string (avoids escape sequence issues)
f = open(r"C:\Users\blk3-308\hmpmanish.txt", "r")

# Read the entire content of the file and print it
print(f.read())

# Close the file after reading
f.close()





# WAP (Write a Program) to open and read a file (one line)

# Open the file in read mode ("r")
# r before the path is a raw string to avoid escape sequence errors
f = open(r"C:\Users\blk3-308\hmpmanish.txt", "r")

# Read only the first line from the file
print(f.readline())

# Close the file after reading
f.close()


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
