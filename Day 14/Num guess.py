import random
def play_game():
    secret = random.randint(1, 10)

    for i in range(1, 5):
        guess = int(input("Enter a number (1 to 10): "))
        if guess == secret:
            print("You Won!")
            break
        elif guess < secret:
            print("Too Low")
        else:
            print("Too High")
    else:
        print("You Lost!")

    print("Secret number was:", secret)
play_game()
