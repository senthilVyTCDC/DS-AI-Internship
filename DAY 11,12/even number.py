limit = int(input("Enter the limit: "))

print(f"Even numbers from 1 to {limit} are:")
for num in range(1, limit + 1):
    if num % 2 == 0:
        print(num)