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