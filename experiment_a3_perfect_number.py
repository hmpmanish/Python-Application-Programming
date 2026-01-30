n=int(input("Enter a number: "))
c=0
while (n!=0):
    r=n%10
    c=c+r*r*r
    n=n//10
    if (n==c):
        print("Perfect Number")