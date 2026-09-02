expenses = {
    "Food": 4500,
    "Travel": 2500,
    "Shopping": 6000,
    "Education": 300,
    "Entertainment": 2000
}

def view():
    print(expenses)

def add():
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))
    expenses[category] = amount

def total():
    return sum(expenses.values())

def highest():
    return max(expenses.values())

def lowest():
    return min(expenses.values())

def average():
    return total() / len(expenses)

def budget():
    b = int(input("Enter budget: "))

    if total() <= b:
        print("Within budget")
    else:
        print("Budget exceeded")

def report():
    print("Total:", total())
    print("Highest:", highest())
    print("Lowest:", lowest())
    print("Average:", average())


print("1. View all expenses")
print("2. Add expense")
print("3. Calculate total")
print("4. Find highest expense")
print("5. Find lowest expense")
print("6. Calculate average")
print("7. Check budget")
print("8. Generate report")
print("9. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    view()

elif choice == 2:
    add()

elif choice == 3:
    print("Total:", total())

elif choice == 4:
    print("Highest:", highest())

elif choice == 5:
    print("Lowest:", lowest())

elif choice == 6:
    print("Average:", average())

elif choice == 7:
    budget()

elif choice == 8:
    report()

elif choice == 9:
    print("Thank you!")

else:
    print("Invalid choice")