# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = """Multi-line
string"""
# Accessing characters
s = "Python"
print(s[0]) # P
print(s[-1]) # n
print(s[1:4]) # yth (slicing)
print(s[ :-1]) # nohtyP (reverse)
# String operations
print(s1 + " " + s2) # Concatenation
print("Ha" * 3) # HaHaHa
print(len(s)) # 6
# String methods
text = " Hello, World! "
print(text.strip()) # "Hello, World!"
print(text.lower()) # " hello, world! "
print(text.upper()) # " HELLO, WORLD! "
print(text.replace("World", "Python"))
print(text.split(",")) # [' Hello', ' World! ']
print("-".join(["a","b","c"])) # "a-b-c"
print("hello".startswith("he")) # True
print("hello".endswith("lo")) # True
print("Hello123".isalnum()) # True
print("Hello".isalpha()) # True
print("12345".isdigit())