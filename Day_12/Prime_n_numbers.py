Limit = int(input("Enter the Limit: "))
def prime_numbers(Limit):
    for i in range(2,Limit):
        num = 1
        for j in range (2,i):
            if (i%j==0 and i!=2):
                num = 0
                break
            else:
                num = 1
        if num == 1:
                print(i)
prime_numbers(Limit)


