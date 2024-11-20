import random

number_of_rolls = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        number_of_rolls += 1
        try:
            num_of_die = int(input("How many die do you want to throw? : "))
            if num_of_die < 0:
                print("Please enter a positive number!")
            else:
                dice_rolls = [random.randint(1, 6) for _ in range(num_of_die)]
                print(", ".join(map(str, dice_rolls)))
        except ValueError:
            print("Invalid input! Please enter a valid number")

    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
print(f"This player rolled {number_of_rolls} time(s)")
