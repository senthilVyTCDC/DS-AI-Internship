import random

limit = int(input("Enter how many times would you like to play this game: "))
choices = ["Stone", "Paper", "Scissor"]

count = 0
count1 = 0
count2 = 0

for i in range(1,limit+1):

    random_choice = random.choice(choices)
    your_choice = input("\nEnter your Choice: ")

    if(random_choice == choices[0] and your_choice == choices[1]):
        print("You Won this round.")
        count = count + 1

    elif(random_choice == choices[0] and your_choice == choices[2]):
        print("You lost this round (Computer Won).")
        count1 = count1 + 1

    elif(random_choice == choices[1] and your_choice == choices[0]):
        print("You lost this round (Computer Won).")
        count1 = count1 + 1

    elif (random_choice == choices[1] and your_choice == choices[2]):
        print("You Won this round.")
        count = count + 1

    elif(random_choice == choices[2] and your_choice == choices[0]):
        print("You Won this round.")
        count = count + 1

    elif(random_choice == choices[2] and your_choice == choices[1]):
        print("You lost this round (Computer Won).")
        count1 = count1 + 1

    else:
        print("This round is drawn")
        count2 = count2 + 1

print("You won :", count, "times")
print("Computer Won: ", count1, "times")
print("Match Drawn :", count2, "times")