start = int(input("Enter the Starting Value: "))
limit = int(input("Enter the Ending Value: "))
if start%2==0:
    for i in range (start, limit+1, 2):
        print(i)
else:
    for i in range (start+1, limit+1, 2):
        print(i)