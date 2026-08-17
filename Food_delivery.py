name=input("Enter customers name: ")
amount=int(input("Enter the amount: "))
distance=float(input("Enter the distance in km: "))
membership=input("Enter the membership status: ")

discount=amount*discount

if distance >= 3:
    print("There is no charge for delivery")
elif distance >=7:
    print("You'll be charged 40$ for delivery")
elif distance >=12:
    print("You'll be charged 70$ for delivery")
else:
    print("You'll be charged 100$ for delivery")
