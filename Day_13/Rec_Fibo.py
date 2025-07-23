num = int(input("Enter the Nth Element : "))

def fibo(num):
    if num <= 0:
        return(0)
    elif num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fibo(num-1) + fibo(num-2))

result = fibo(num)
print("The Element", num,"of Fibonacci Series is: ", result)