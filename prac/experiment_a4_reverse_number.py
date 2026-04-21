s=0
n=int(input("Enter a number: "))
while(n!=0):
    r=n%10
    s=r+s*10
    n=n//10
print("Reversed Number is:",s)