# hmpmanish
# Experiment 9: Password validation system using for loop

correct_password = "python123"  # Set the correct password
attempts = 3                     # Total allowed attempts

for i in range(attempts):
    pwd = input("Enter password: ")  # Ask user for password
    if pwd == correct_password:      # Check if correct
        print("Access granted!")     # Success
        break
    else:
        print("Incorrect password!") # Wrong attempt
else:
    # This else runs if loop completes without break
    print("Attempts exhausted. Access denied.")
