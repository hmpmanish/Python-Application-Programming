# File name: area_of_circle.py

# create class

class Area:  # class names should be capitalized by convention
    radius = 0  # data member

    def circle(self):  # circle is the member function
        a = 3.14 * self.radius * self.radius  # use self.radius
        print("Area is", a)


# create object
A1 = Area()  # A1 is the object
A1.radius = 3
A1.circle()  # Output: Area is 28.26

# Note:
# 'self' is a compulsory argument in every instance method.
# It holds the reference of the object that calls the method.





# File name: area_of_circle_v2.py

class AreaOfCircle:
    def __init__(self, radius):
        self.radius = radius

    def circle(self):
        a = 3.14 * self.radius * self.radius
        print("Area is", a)

# create objects
A1 = AreaOfCircle(3)
B1 = AreaOfCircle(5)

A1.circle()  # Area is 28.26
B1.circle()  # Area is 78.5
