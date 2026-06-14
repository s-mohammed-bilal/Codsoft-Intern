import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def find_winner(user, computer):

    if user == computer:
        return "Tie"

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "User"

    else:
        return "Computer"


print("===== ROCK PAPER SCISSORS =====")

while True:

    user_choice = input(
        "\nEnter Rock, Paper or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid Input!")
        continue

    computer_choice = random.choice(choices)

    print("Your Choice     :", user_choice)
    print("Computer Choice :", computer_choice)

    result = find_winner(user_choice, computer_choice)

    if result == "Tie":
        print("Match Tied!")

    elif result == "User":
        print("You Won!")
        user_score += 1

    else:
        print("Computer Won!")
        computer_score += 1

    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        break

print("\n===== FINAL SCORE =====")
print("You      :", user_score)
print("Computer :", computer_score)