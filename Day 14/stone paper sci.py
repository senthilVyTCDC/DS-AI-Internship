from random import choice
choices = ["Stone", "Paper", "Scissor"]
rounds = int(input("How many rounds: "))
user_wins = 0
comp_wins = 0
draws = 0
for i in range(rounds):
    user = input("\nEnter your choice (Stone/Paper/Scissor): ").capitalize()
    if user not in choices:
        print("Invalid choice, round skipped.")
        continue

    comp = choice(choices)
    print("Computer chose:", comp)

    if user == comp:
        print("Draw")
        draws += 1
    elif (choices.index(user) - choices.index(comp)) % 3 == 1:
        print("You Won!")
        user_wins += 1
    else:
        print("Computer Won!")
        comp_wins += 1
print("\nGame Over!")
print("You:", user_wins)
print("Computer:", comp_wins)
print("Draws:", draws)
