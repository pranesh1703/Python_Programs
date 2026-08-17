name = input("Enter your name: ")
pin = int(input("Enter your PIN: "))

correct_pin = 1234
balance = 1000

if pin == correct_pin:
    print("Welcome", name)

    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is ₹", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount > balance:
            print("Insufficient balance")

        elif amount % 100 != 0:
            print("Amount must be a multiple of 100")

        else:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance: ₹", balance)

            if balance < 200:
                print("WARNING: Your balance is below ₹200")

    elif choice == 3:
        print("Thank you for using the ATM")

    else:
        print("Invalid choice")

else:
    print("Incorrect PIN")