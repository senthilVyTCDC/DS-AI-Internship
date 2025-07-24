import random

start_num = int(input("Enter the Starting number that you would like to set as limit: "))
end_num = int(input("Enter the Ending number that you would like to set as limit: "))

count = 0
random_number = random.randint(start_num,end_num)
for i in range(1,5):
    Num = int(input("\nEnter any number: "))

    if(Num==random_number):
        print("\nYou Won the Game")
        count = count + 1
        break

    elif(Num<random_number):
        print("Too Low")
        count = count + 1

    elif(Num>random_number):
        print("Too High")
        count = count + 1

    else:
        print("Invalid Number")

print("\nTotal Guesses: ",count)

print("\nRandom Number: ",random_number)

if count == 4:
    if Num != random_number:
        print("\nYou Lost the Game (Computer WON)")




