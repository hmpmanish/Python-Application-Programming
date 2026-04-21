n = int(input("Enter a numerator: ")) 
d = int(input("Enter a denominator: "))
try:
    c = n / d
    print("quotientis:", c)
except:
    print("ddenominator can not be zero ")
