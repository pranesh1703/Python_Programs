name = input("Enter customer name: ")
price = float(input("Enter product price: "))
product=input("Enter the product: ")
quantity = int(input("Enter quantity: "))
membership = input("Enter membership type (regular/premium): ").lower()

total = price * quantity

if membership == "premium" and total >= 5000:
    discount = total * 0.20
elif membership == "premium" and total >= 2000:
    discount = total * 0.15
elif membership == "regular" and total >= 5000:
    discount = total * 0.10
else:
    discount = total * 0.05

final_amount = total - discount

print("----- BILL -----")
print("Customer Name:", name)
print("Products bought:",product)
print("Total Amount: $", total)
print("Discount: $", discount)
print("Final Amount: $", final_amount)