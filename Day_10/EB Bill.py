Unit = int(input("Enter Units: "))
Unit = abs(Unit)
charge = 0
if Unit <= 100:
    charge = 0
elif Unit <= 200:
    charge = (Unit - 100) * 1.5
elif Unit <= 300:
    charge = (Unit - 100) * 2
elif Unit <= 400:
    charge = (Unit - 100) * 2.5
else:
    charge = (Unit - 100) * 3
print("Total Charges = ", charge)
