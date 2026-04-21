# hmpmanish
# Experiment 5: ATM minimum number of notes

amount = int(input("Enter amount: "))

n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100

print("2000 notes:", n2000)
print("500 notes:", n500)
print("200 notes:", n200)
print("100 notes:", n100)
