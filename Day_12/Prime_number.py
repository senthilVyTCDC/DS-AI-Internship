Num = int(input("Enter any Number: "))
num = 0
for i in range (1,Num):
    if (Num%i==0 and Num!=2):
        num = 1
        break

if num == 1:
    print(Num, "is not a Prime Number")
else:
    print(Num, "is a Prime Number")


