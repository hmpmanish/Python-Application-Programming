# hmpmanish
# Experiment 8: Print all even numbers from 1 to 100 and count

count = 0

for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
        count += 1

print("\nTotal even numbers:", count)
