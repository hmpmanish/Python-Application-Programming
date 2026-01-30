# hmpmanish
# Program to print even numbers between two numbers and count them

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

even_numbers = []
count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)
        count += 1

print("Even numbers:", even_numbers)
print("Total even numbers:", count)
