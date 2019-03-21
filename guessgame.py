import random
number_of_guesses = 0
number = random.randint(1,100)

name = input("Hello! What is your name? ")

print(name + ", I am thinking of a number between 1 and 100. Can you guess what number it is?")

while number_of_guesses < 5:
    guess = input("Take a guess ")
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1;
    number_of_guesses_remaining = 5 - number_of_guesses;
    if guess < number:
        number_of_guesses_remaining = str(number_of_guesses_remaining)
        print("Your guess is too low! You have " + number_of_guesses_remaining + " number_of_guesses_remaining ")
    if guess > number:
        number_of_guesses_remaining = str(number_of_guesses_remaining) 
        print("Your guess is too high! You have " + number_of_guesses_remaining + " number_of_guesses_remaining ")
    if guess == number:
        break
if guess == number:
    number_of_guesses = str(number_of_guesses)
    print("cheers! You guessed the number in " + number_of_guesses + " tries :)")

if guess != number:
    number = str(number)
    print("Oops! Better luck next time " + name + " the number i was thinking of is " + number + " :) ")
