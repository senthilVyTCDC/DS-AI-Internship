num = input("Enter a number: ")

if len(num) <= 2:
    print("Not a Xylem number (needs at least 3 digits)")
else:
    first = int(num[0])
    last = int(num[-1])
    middle_sum = sum(int(digit) for digit in num[1:-1])

    if first + last == middle_sum:
        print("It is a Xylem number")
    else:
        print("It is not a Xylem number")
