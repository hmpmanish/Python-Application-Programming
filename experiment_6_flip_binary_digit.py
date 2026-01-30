# hmpmanish
# Experiment 6: Flip one digit to make all digits same

A = input("Enter binary number: ")

count0 = A.count('0')
count1 = A.count('1')

if count0 == 1 or count1 == 1:
    print("YES")
else:
    print("NO")
