Num = int(input("Enter any number: "))
N = Num
R = 0
while (N!=0):
        R = R * 10 + N % 10
        N = N//10
print("Reversed Number: ", R)

if(R==Num):
    print(Num, "is palindrome.")
else:
    print(Num, "not a palindrome.")

