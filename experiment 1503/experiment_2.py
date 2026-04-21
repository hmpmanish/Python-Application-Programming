"""
Question 2: Write a Python program to determine eligibility for the End Term Exam (ETE) 
based on scores in three consecutive assignments using nested if-else statements.
""" 
"""#HMPMANISH """


# Input marks for Assignment 1
a1_score = int(input("Enter assignment 1 marks: "))

if a1_score >= 75:
    print("You are eligible for assignment 2")
    
    # Input marks for Assignment 2
    a2_score = int(input("Enter assignment 2 marks: "))
    
    if a2_score > 65:
        print("You are eligible for assignment 3")
        
        # Input marks for Assignment 3
        a3_score = int(input("Enter assignment 3 marks: "))
        
        if a3_score >= 55:
            print("You are eligible for ETE")
        else:
            print("Not eligible for ETE")
            
    else:
        print("Not eligible for assignment 3")
        
else:
    print("Not eligible for assignment 2")