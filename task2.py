a=int(input("Enter the first value: "))
b=int(input("Enter the second value:"))
print("Before swapping a",a,"\nBefore swapping b",b)
temp=a
a=b
b=temp
print("After swapping a",a,"\nAfter swapping b",b)


a=int(input("Enter the first value: "))
b=int(input("Enter the second value:"))
print("Before swapping a",a,"\nBefore swapping b",b)
b=b-a
a=b+a
print("After swapping a",a,"\nAfter swapping b",b)