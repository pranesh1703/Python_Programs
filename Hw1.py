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

#Finding a prime number
a = int(input("Enter a number: "))

if a < 2:
    print("Not a prime number")
else:
    for i in range(2, a):
        if a % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#Finding factorial 
a=int(input("Enter a value: "))
for i in range (1,a):
    print(i)
fact=1
for i in range (1,a):
    fact=fact*i
    print(fact)
