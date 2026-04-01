# create class
class AreaOfCircle:
    def message(self, radius):
        a = 3.14 * radius * radius
        print("Area is", a)

# create objects
A1 = AreaOfCircle()
B1 = AreaOfCircle()

# call method correctly
A1.message(3)
B1.message(5)
