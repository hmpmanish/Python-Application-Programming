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