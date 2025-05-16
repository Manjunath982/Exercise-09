import random


def get_user_choice():
    print("Enter your choice: Snake, Water, or Gun")
    user_choice = input().strip().capitalize()
    if user_choice in ["Snake", "Water", "Gun"]:
        return user_choice
    else:
        print("Invalid choice. Please choose Snake, Water, or Gun.")
        return get_user_choice()


def get_computer_choice():
    return random.choice(["Snake", "Water", "Gun"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Snake" and computer_choice == "Water") or \
         (user_choice == "Water" and computer_choice == "Gun") or \
         (user_choice == "Gun" and computer_choice == "Snake"):
        return "User"
    else:
        return "Computer"


def print_result(winner, user_choice, computer_choice):
    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    if winner == "Draw":
        print("It's a draw!")
    elif winner == "User":
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")


def main():
    print("Welcome to the Snake, Water, Gun Game")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)
    print_result(winner, user_choice, computer_choice)


if __name__ == "__main__":
    main()
