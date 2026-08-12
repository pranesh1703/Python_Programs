#Finding odd numbers
a=int(input("Enter a value: "))
if (a%2!=0):
    print("It's an odd number")
else:
    print("It's not an odd number")

#Finding an even number
a=int(input("Enter a value: "))
if (a%2==0):
    print("It's an even number")
else:
    print("It's not an even number")    

#Finding the Ascending order
a=int(input("Enter a value: "))
for i in range (1,a):
        print(i)

#Finding the Descending order
a=int(input("Enter a value: "))
for i in range (a,0,-1):
        print(i)
