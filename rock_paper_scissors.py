import random

choices = ("r", "p", "s")
emojis = {"r": "🥌", "p": "🧻", "s": "✂"}
no_of_rounds = int(input("Enter no of rounds to be played: "))


def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid options")


def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice


def display_choice(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
        return "Tie!"
    elif user_choice == "r" and computer_choice == "s" or user_choice == "s" and computer_choice == "p" or user_choice == "p" and computer_choice == "r":
        print("You won! 🥇🏆")
        return "user"

    else:
        print("🔥🔥 Ooops, you lose! 😒")
        return "computer"


def main():
    user_wins = 0
    computer_wins = 0
    rounds_played = 0

    while rounds_played < no_of_rounds:
        print(f"\n---- Round {rounds_played + 1} ----")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choice(user_choice, computer_choice)
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        rounds_played += 1
        print(f"Score You: {user_wins} - Computer: {computer_wins}")

        # Check if it's already impossible for the other player to win
        remaining_rounds = no_of_rounds - rounds_played
        if user_wins > computer_wins + remaining_rounds:
            print("\n🎉 You are the overall winner!")
            break
        elif computer_wins > user_wins + remaining_rounds:
            print("\n💻 The computer is the overall winner!")
            break

    # Determine the Overall winner:
    if user_wins > computer_wins:
        print(f"\n🎉 Congratulations! You are the overall winner!. with {
              user_wins} points")
    elif computer_wins > user_wins:
        print(f"\n💻 The computer is the overall winner. Better luck next time!. with {
              computer_wins} points")
    else:
        print("\n🤝 It's a draw after 3 rounds!")
    print("Game over!")


main()
