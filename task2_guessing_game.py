import random

def number_guessing_game():
    print("\n🎲 Welcome to the Number Guessing Challenge! 🎲")
    print("Choose a difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        number = random.randint(1, 50)
        attempts_left = 10
        upper = 50
    elif choice == "2":
        number = random.randint(1, 100)
        attempts_left = 7
        upper = 100
    else:
        number = random.randint(1, 200)
        attempts_left = 5
        upper = 200

    print(f"\n🔢 I have chosen a number between 1 and {upper}. Can you guess it?")
    print(f"You have {attempts_left} attempts. Good luck! 🍀\n")

    while attempts_left > 0:
        try:
            guess = int(input("👉 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts_left -= 1

        if guess == number:
            score = attempts_left * 10
            print(f"🎉 Congratulations! You guessed the number {number} correctly.")
            print(f"🏆 Your score: {score}")
            break
        elif guess < number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        # Provide a hint if close
        if abs(number - guess) <= 5:
            print("💡 Hint: You're very close!")

        if attempts_left > 0:
            print(f"⏳ Attempts left: {attempts_left}\n")
        else:
            print(f"❌ Out of attempts! The correct number was {number}.\n")

    play_again = input("🔁 Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        number_guessing_game()
    else:
        print("👋 Thanks for playing! Goodbye.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
