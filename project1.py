import random

print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100.")
print("Try to guess the number in as few attempts as possible.")

number = random.randint(1, 100)


guesses = 0


while True:
   
    guess = int(input("Enter your guess: "))
    guesses += 1

   
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "guesses!")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
