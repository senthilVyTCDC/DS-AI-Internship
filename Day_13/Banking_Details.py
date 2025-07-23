def Dep(tot_amt): #with argument without return type
    dep_amt = int(input("Enter the amount to Deposit: "))
    print("\nAmount:", dep_amt, "is deposited.")
    tot_amt += dep_amt
    return tot_amt

def Wd(with_amt, tot_amt): #with argument, with return type
    if with_amt > tot_amt:
        print("\nInsufficient Balance!")
        return tot_amt
    else:
        print("\nAmount:", with_amt, "is Withdrawn.")
        return tot_amt - with_amt

def Ad(): #without argument without return type
    name = "Vijayabhaskar"
    acc_num = "2127220502"
    age = "20"
    con_num = "8754300000"
    print("Name:", name)
    print("Account Number:", acc_num)
    print("Age:", age)
    print("Contact Number:", con_num)

def Bl(): #without argument with return type
    global tot_amt
    return tot_amt

tot_amt = 0
var = ""

while var!="END":
    print("\n1. Deposit 2. Withdrawal 3. Account Details 4. Balance")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        tot_amt = Dep(tot_amt)

    elif choice == 2:
        with_amt = int(input("\nEnter the amount to withdraw: "))
        tot_amt = Wd(with_amt, tot_amt)

    elif choice == 3:
        Ad()

    elif choice == 4:
        bal_amt = Bl()
        print("\nBalance Amount:", bal_amt)

    else:
        print("\nEnter a valid option between 1 and 4")

    var = input("\nEnter 'END' to exit the loop or press Enter to continue: ")
