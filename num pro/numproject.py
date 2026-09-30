import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 1000)
attempts = 0

print("=================================")
print("   NUMBER GUESSING GAME")
print("=================================")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number:", secret_number)
        print("Total attempts:", attempts)
        break