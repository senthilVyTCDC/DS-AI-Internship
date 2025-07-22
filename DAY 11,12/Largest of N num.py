n = int(input("How many numbers? "))

numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
