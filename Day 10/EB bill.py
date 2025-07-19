units = int(input("Enter the number of units: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 1.5
elif units <= 300:
    bill = (units - 100) * 2
elif units <= 400:
    bill = (units - 100) * 2.5
else:
    bill = (units - 100) * 3

print("Your EB Bill is Rs.", bill)
