limit = int(input("Enter the limit: "))
num1 = 0
num2 = 1
for i in range(0,limit,1):
    print(num1)
    num3 = num1+num2
    num1 = num2
    num2 = num3
    if limit == i:
        break

