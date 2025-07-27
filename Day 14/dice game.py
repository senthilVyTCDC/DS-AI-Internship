from random import randint
rounds = int(input("How many rounds: "))
user_wins = 0
computer_wins = 0
draws = 0
for i in range(1, rounds + 1):
    user = int(input("\nEnter a number between 1 and 6: "))
    computer = randint(1, 6)
    print("Computer rolled:", computer)

    if user == computer:
        print("You Win!")
        user_wins += 1
    elif (user % 2 == computer % 2):
        print("It's a Draw!")
        draws += 1
    else:
        print("Computer Wins!")
        computer_wins += 1
print("\nGame Over!")
print("You Won:", user_wins)
print("Computer Won:", computer_wins)
print("Draws:", draws)
