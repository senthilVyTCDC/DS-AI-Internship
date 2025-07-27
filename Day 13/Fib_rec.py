def fib_recursive(count):
    if count <= 0:
        return 0
    elif count == 1:
        return 0
    elif count == 2:
        return 1
    else:
        a = fib_recursive(count - 1)
        b = fib_recursive(count - 2)
        return a + b

index = int(input("Which Fibonacci element do you want? "))
result = fib_recursive(index)
print("Result for position", index, "is:", result)