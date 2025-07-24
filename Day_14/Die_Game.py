import random

limit = int(input("Enter how many times should the die rolled: "))
count = 0
count1 = 0
count2 = 0

for i in range(1,limit+1):
    random_number = random.randint(1, 6)
    user_input = int(input("\nEnter any Number: "))
    if (user_input == random_number):
        print("You Won the Game")
        count = count + 1

    elif (user_input != random_number):

        if (user_input % 2 == 0 and random_number % 2 == 0):
            print("Draw")
            count2 = count2 + 1

        elif (user_input % 2 != 0 and random_number % 2 != 0):
            print("Draw")
            count2 = count2 + 1
        else:
            print("You Lost the Game (Computer Won)")
            count1 = count1 + 1

    else:
        print("Invalid input")

print("\nYou Won:", count, "times out of", limit)
print("Computer Won:", count1, "times out of", limit)
print("Match Drawn:", count2, "times out of", limit)



