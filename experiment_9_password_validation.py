# hmpmanish
# Experiment 9: Password validation system (3 attempts)

correct_password = "python123"
attempts = 3

for i in range(attempts):
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted!")
        break
    
    else:
        print("Incorrect password!")
else:
    print("Attempts exhausted. Access denied.")
