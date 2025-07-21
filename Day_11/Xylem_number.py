Num = int(input("Enter a number: ")) #23337
N = Num #23337
last_digit = Num % 10 #7
Num = Num // 10 #2333
middle_sum = 0

while Num > 9: #233, 23, 2
    rem = Num % 10 #3, 3,
    middle_sum += rem #3, 6,-> 9
    Num = Num // 10 #233

first_digit = Num #2

extreme_sum = first_digit + last_digit #9

if extreme_sum == middle_sum:
    print(N, "is a Xylem number.")
else:
    print(N, "is not a Xylem number.")
