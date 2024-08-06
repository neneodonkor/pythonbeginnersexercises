# This is a sample Python script.

import random

if __name__ == '__main__':
    print("\n")
    print("Python Workouts!")
    print("------------------------------")

# This is simple game whereby the computer tries to guess the number in my head.
# First, the lowest and highest numbers are set. The index, which relates to number
# of guesses is set to zero. The guessNumber() is called to get the first random
# number. The checkGuess() is called to verify if the guess is higher than the
# number, lower than the number, or the exact number.
#
# The random number function is modified by updating the lows and highs for
# randint() after each iteration. The number of guesses is also passed on after
# each guess.

number = int(input("What is the number in your head? "))

low, high, idx = 0, 100, 0


def guessNumber(lo: int, hi: int) -> int:
    return random.randint(lo, hi)


def checkGuess(lo: int, hi: int, rand: int, index: int) -> None:
    lo = lo
    hi = hi
    number_of_guesses = index

    response = (
        input(
            f"Is '{rand}' too high, too low, or the exact number? Use 'H', 'L', or 'E' to answer: "
            f"").upper())

    if response == 'H':
        print(f"The number '{rand}' is too high\n")
        number_of_guesses += 1
        hi = rand - 1
        rand = guessNumber(lo, hi)
        checkGuess(lo, hi, rand, number_of_guesses)

    if response == 'L':
        print(f"The number '{rand}' is too low\n")
        number_of_guesses += 1
        lo = rand + 1
        rand = guessNumber(lo, hi)
        checkGuess(lo, hi, rand, number_of_guesses)

    if response == 'E':
        print("You guessed the correct answer!")
        print(f"You guessed {number_of_guesses + 1} time(s)")
        return


guess = guessNumber(low, high)
checkGuess(low, high, guess, idx)
