mobile_number=int(input("Enter your Mobile number: "))

print("\n------------Recharge Price--------------")
print("199 = 1.0GB per day")
print("299 = 1.5GB per day")
print("399 = 2.0GB per day")
print("499 = 2.5GB per day")
print("599 = 3.0GB per day")

recharge_amount=int(input("Enter the recharge amount: "))
recharge_type=input("Enter the recharge type (Prepaid/Postpaid): ")

total=recharge_amount
discount=0

if recharge_type=="prepaid" and recharge_amount==199:
    print("Your Prepaid plan is 1GB for 199")
elif recharge_type=="prepaid" and recharge_amount==299:
    print("Your Prepaid plan is 1.5GB for 299")
elif recharge_type=="prepaid" and  recharge_amount==399:
    print("Your Prepaid plan is 2GB for 399")
elif recharge_type== "prepaid" and recharge_amount==499:
    print("Your Prepaid plan is 2.5GB for 499")
elif recharge_type== "prepaid" and recharge_amount==599:
    print("Your Prepaid plan is 3GB for 599")
elif recharge_type=="postpaid" and recharge_amount==199:
    print("Your Postpaid plan is 1GB for 199")
elif recharge_type== "postpaid" and recharge_amount==299:
    print("Your Postpaid plan is 1.5GB for 299")
elif recharge_type== "postpaid" and  recharge_amount==399:
    print("Your Postpaid plan is 2GB for 399")
elif recharge_type== "postpaid" and recharge_amount==499:
    discount=total * 0.15
    print("Your Postpaid plan is 2.5GB for 499")
elif recharge_type== "postpaid" and recharge_amount==599:
    discount=total * 0.15
    print("Your Postpaid plan is 3GB for 599")
else:
    print("Invalid recharge plan")

final_amount=total - discount

print("\n-----------BILL----------")
print("Your Mobile number is: ",mobile_number)
print("Your recharge amount is: ",recharge_amount)
print("Your recharge type is: ",recharge_type)
print("Final amount: ",final_amount)













