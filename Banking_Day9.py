import mysql.connector

ps = input("Enter your MySQL Password: ")

# Step 1: Connect to MySQL and specify the database directly
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    port=3306,
    database='banking'
)

cursor = connect.cursor()

# Step 2: Create 'customers' table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    customer_account_no BIGINT UNIQUE,
    customer_mobile_number BIGINT,
    account_balance DECIMAL(10, 2)
)
""")
print("Table 'customers' created (if it didn’t exist already).\n")

# Step 3: Insert sample customers
insert_query = """
INSERT IGNORE INTO customers (customer_name, customer_account_no, customer_mobile_number, account_balance)
VALUES (%s, %s, %s, %s)
"""

customers_data = [
    ('John', 5566751, 9876534450, 50000.00),
    ('Nick', 7788990, 9876534451, 35000.00),
    ('Fury', 1234567, 9876534452, 20000.00),
    ('Alex', 7654321, 9876534453, 45000.00),
    ('Raj', 9988776, 9876534454, 10000.00),
]

for customer in customers_data:
    cursor.execute(insert_query, customer)

connect.commit()
print("Sample customers inserted (if not already present).\n")

# Step 4: Ask for account number and operation
acc_no = int(input("Enter your Account Number: "))

cursor.execute("SELECT * FROM customers WHERE customer_account_no = %s", (acc_no,))
customer = cursor.fetchone()

if customer:
    customer_id, name, account_no, mobile, balance = customer
    print("\nWelcome", name, "\n")
    choice = input("Enter your choice (1. Withdraw or 2. Deposit): ")

    if choice == '1':
        amount = float(input("\nEnter amount to withdraw: "))
        if amount > balance:
            print("\nInsufficient balance.")
        else:
            cursor.execute("UPDATE customers SET account_balance = account_balance - %s WHERE customer_account_no = %s", (amount, acc_no))
            connect.commit()
            print("\nWithdrawal successful.")

    elif choice == '2':
        amount = float(input("\nEnter amount to deposit: "))
        cursor.execute("UPDATE customers SET account_balance = account_balance + %s WHERE customer_account_no = %s", (amount, acc_no))
        connect.commit()
        print("\nDeposit successful.")

    else:
        print("\nInvalid option.")
else:
    print("\nAccount not found.")

# Step 5: Close connection
cursor.close()
connect.close()
print("\nConnection closed.")