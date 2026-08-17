# Finding the area and perimeter of the rectangle
a=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the width of the rectangle: "))
area=a*b
print(area)

a=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the width of the rectangle: "))
area=a*b
print("The area of the rectagle is: ",area)


a=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the width of the rectangle: "))
area=a*b
print(type(area))
print("The area of rectangle is %d"%(area))

a=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the width of the rectangle: "))
peri=2*(a*b)
print(type(peri))
print("The perimeter of rectangle is %d"%(peri))


# Swapping with and without variable
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



# Voting system
age=int(input("Enter the age: "))
if (age>=18):
    print("You're eligible to vote")
else:
    print("You're not eligible to vote")    



# Verifying the greater number
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




# Leap year
year=int(input("Enter the year: "))
if (year%4==0):
    print("It's a leap year")
else:
    print("It's not a leap year")   




#Reverse star order
a = int(input("Enter number rows: "))
for i in range(a, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()



#number
a = int(input("Enter number rows: "))
for i in range(a, 0, -1):
    for j in range(1, i + 1):
        print(i, end="")
    print()


#number
a = int(input("Enter number rows: "))
for i in range(a, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



# String format
name="Pranesh"
department="B.Tech CSE AI&ML"
age=18
cgpa=8.1
print("hi welcome")
print("Im",name ,"\nand im from",department, "\tmy age is",age, "my cgpa is",cgpa)
print("Im %s\nand im from%s \tmy age is%d my cgpa is%f"%(name,department,age,cgpa))
print("Im {}\nand im from{} \tmy age is{} my cgpa is{}".format(name,department,age,cgpa))


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
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")


#Finding factorial 
a=int(input("Enter a value: "))
fact=1
for i in range (1,a):
    fact=fact*i
    print(fact)


#For star pattern
a=int(input("Enter number rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*", end= " ")
    print()



#For number
a=int(input("Enter number rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i, end= " ")
    print()



#For number
a=int(input("Enter number rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j, end= " ")
    print()


#For number
a=int(input("Enter number rows: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(a, end= " ")
    print()


#For number
a=int(input("Enter number rows: "))
num=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(num, end= " ")
        num=num+1
    print()    



# Identity operators
str1 ="hello"
str2="welcome"
print(id(str1))
print(id(str2))

str5="kg"
str6="kg"

print(id(str5))
print(id(str6))

print(id(str5) is not id(str6))
print(str5 is str6)

word ="Python is high level programming language"
print("Python" in word)

print("hi welcome",sep="-")
print("python class")



date=13
month=8
year=2026
print(date,month,year,sep="-")



#type conversions


a1=10
con = float(a1)
print(con)
print(type(con))


#input during the runt time

department=input("Enter Department: ")
print("Im pursuing",department)

#Operators
#Arithmetic operators  +,-,*,/,%,//,**

a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(-10//20)
print(2**3**5)

#Relational operator
#=,+=,-=,*=,/=,%=,//=,**=,&=,|=,^=,<<=,>>=




# String methods
str1="Pranesh"
print(str1.rstrip("h"))
print(str1.lstrip("P"))
print(str1.strip())



str2="17-08-2026"
print(str2.split("-",1))
print(str2.split("-"))


str3="Python is a high level programing language"
print(str3.replace("Python","Java"))



str4=["S.","Pranesh"]
print("_".join(str4))



str5="Programing"
print(str5.endswith("ing"))
print(str5.startswith("Pro"))
