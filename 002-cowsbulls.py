# This is a sample Python script.

# The Cowbull game is a popular guessing game that involves numbers.
# Here's a brief overview:
#
# - One player thinks of a 4-digit number and keeps it secret.
# - The other player tries to guess the number by suggesting a 4-digit number.
# - For each digit in the guessed number, the first player gives feedback in the form of:
#       - Cow: If a digit is in the correct position in the secret number.
#       - Bull: If a digit is in the secret number, but not in the correct position.
# - The guesser uses this feedback to refine their next guess.
# - The game continues until the guesser correctly guesses the secret number.
#
# Example: Secret number: 1234 Guessed number: 1243 Feedback: 2 Cows (1 and 2 are in the correct
# position), 2 Bulls (3 and 4 are in the secret number, but not in the correct position) The
# Cowbull game requires strategic thinking and deduction skills. It's a fun and challenging game
# that can be played with friends or online.
#
# However, in this example, I display the random number. Obviously, it is supposed to be
# not hidden. But in order to see it work that is why it is shown.

import random

if __name__ == '__main__':
    print("\n")
    print("Python Workouts!")
    print("------------------------------")


def getRandomNumber():
    random_number = str(random.randint(1000, 9999))

    # The for-loop is to ensure that the 4-digit number
    # does not contain any duplicate number such as 1145.
    # If it does, the function is called again.
    for char in random_number:
        if random_number.count(char) > 1:
            return getRandomNumber()

    # This is a second method of solving the proble.
    # In this case the index is used to know if a duplicate
    # exists up to the current iteration: random_number[:idx]
    #
    # for idx, char in enumerate(random_number):
    #     if char in random_number[:idx]:
    #         return getRandomNumber()

    return random_number


randomnumber = getRandomNumber()
print("Random number: " + randomnumber)

while True:
    guess = ''
    cows, bulls = 0, 0

    # The inner while loop is to make sure that the input entered
    # is a 4-digit number
    while True:
        guess = input("Guess the 4-digit number (type '0000' to exit): ").lower()

        if len(guess) == 4 and guess.isdigit():
            break

    # Option to exit the game
    if guess == '0000':
        print("You exited the game!")
        break

    for i in range(len(randomnumber)):
        if randomnumber[i] in guess:
            if randomnumber[i] == guess[i]:
                cows += 1
            else:
                bulls += 1

    # This is a second way of doing it.
    # 
    # for i in range(len(randomnumber)):
    #     if randomnumber[i] == guess[i]:
    #         cows += 1
    #     elif randomnumber[i] in guess:
    #         bulls += 1

    print(f"Cows: {cows}   ||   Bulls: {bulls}\n")

    if guess == randomnumber:
        print("You won the game!")
        break
