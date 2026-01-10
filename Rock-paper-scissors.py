import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choices: rock / paper / scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print("User choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: You Lose!")
        computer_score += 1

    print("\nScore")
    print("User:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break