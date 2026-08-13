a=int(input("Enter a value: "))
x=-1
y=1
for i in range(1,a+1):
    z=x+y
    x=y
    y=z
    print(z)
