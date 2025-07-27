def credit(balance):
    amount = int(input("Enter amount to credit: "))
    balance += amount
    print("Credited amount:", amount)
    return balance

def debit(balance):
    amount = int(input("Enter amount to debit: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Debited amount:", amount)
    return balance

def display_info():
    customer = "Parivel"
    acc_no = "7766554433"
    dob = "15-08-2002"
    phone = "9123456789"
    print("Customer Name:", customer)
    print("Account Number:", acc_no)
    print("Date of Birth:", dob)
    print("Phone Number:", phone)

def get_balance(balance):
    return balance

bank_balance = 2540

while True:
    print("\nSelect an operation:")
    print("1. Credit")
    print("2. Debit")
    print("3. Show Details")
    print("4. Show Balance")
    print("5. Exit")

    option = int(input("Enter your option (1-5): "))

    if option == 1:
        bank_balance = credit(bank_balance)
    elif option == 2:
        bank_balance = debit(bank_balance)
    elif option == 3:
        display_info()
    elif option == 4:
        print("Account Balance:", get_balance(bank_balance))
    elif option == 5:
        print("Thank you for using the banking system!")
        break
    else:
        print("Invalid input. Please choose a number between 1 and 5.")
