last = int(input("Enter the last number: "))

print("Prime numbers from 0 to", last," are:")

for num in range(2, last + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
