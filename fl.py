f = open(r"C:\Users\Manish Pandey\Desktop\sample.txt", "w")
f.write("Hello, File!\n")
f.write("Second line\n")
f.close()


f = open(r"C:\Users\Manish Pandey\Desktop\sample.txt", "r")
content = f.read()
f.close()
print(content)

f = open(r"C:\Users\Manish Pandey\Desktop\sample.txt", "a")
