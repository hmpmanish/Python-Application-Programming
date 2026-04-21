# hmpmanish
# Program to check if a number is a palindrome

n = int(input("Enter a number: "))
temp = n  # store original number
s = 0

while temp != 0:
    r = temp % 10
    s = s * 10 + r
    temp = temp // 10

if n == s:
    print(n, "is a Palindrome Number")
else:
    print(n, "is not a Palindrome Number")
