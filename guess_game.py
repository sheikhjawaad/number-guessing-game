import random

print("🎮 Welcome to Number Guessing Game!")

# Choose difficulty
level = input("Choose level (easy/hard): ").lower()

if level == "easy":
    number = random.randint(1, 50)
    max_attempts = 7
else:
    number = random.randint(1, 100)
    max_attempts = 5

attempts = 0

print(f"You have {max_attempts} attempts. Start guessing!")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
        elif guess > number:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

    except ValueError:
        print("⚠️ Please enter a valid number!")

if attempts == max_attempts and guess != number:
    print(f"❌ Game Over! The correct number was {number}")