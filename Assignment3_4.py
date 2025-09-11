import random

secret_number = random.randint(1, 10)
guessed_correctly = False

print("Guess the number between 1 and 10!")

while not guessed_correctly:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Correct! You guessed the number.")
            guessed_correctly = True
    else:
        print("Please enter a valid number.")
