import random

guess = random.randint(1, 20)
MAX_ATTEMPTS = 5
attempt_count = 0

while attempt_count < MAX_ATTEMPTS:
    try:
        user_guess = int(input("Guess the number (between 1 and 20): "))
        attempt_count += 1
        if user_guess < 1 or user_guess > 20:
            print("Number is bewteen 1 and 20")
            continue
        if user_guess < guess:
            print("Too low! Try again")
        elif user_guess > guess:
            print("Too high! Try again")
        else:
            print(f"Congratulations!! You guess the number in {
                  attempt_count} attempts")
            break
        print(f"You have {MAX_ATTEMPTS -
              attempt_count} of attempts remaining.")
    except ValueError:
        print("Invalid input!!")

    if MAX_ATTEMPTS == attempt_count and user_guess != guess:
        print(f"Game over! The correct number was {guess}.")
