# student_marks.py

# Parent class
class Student:
    def __init__(self, name):
        self.name = name   # store student name


# Child class (inherits from Student)
class Marks(Student):
    def __init__(self, name, marks):
        super().__init__(name)   # call parent constructor
        self.marks = marks       # store marks

    def display(self):
        # display student details
        print("Name:", self.name)
        print("Marks:", self.marks)


# Object creation
s1 = Marks("Manish", 95)

# Call display method
s1.display()
