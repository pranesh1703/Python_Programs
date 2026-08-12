a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
c=int(input("Enter the third value: "))
if (a>b and a>c):
    print("A is greater")
elif (b>a and b>c):
    print("B is greater")
elif (c>a and c>b):
    print("C is greater")
else:
    print("All are equal")            