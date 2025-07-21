largest = 0
while True:
    n = input("Enter number (or 'end' to stop): ")
    if n == "end":
        break
    num = int(n)
    if num > largest:
        largest = num

print("Largest number is:", largest)
