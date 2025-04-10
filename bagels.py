import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    # instructions
    print(
        """I am guessing {} digit number with no repeated digits.
          Try to guess what is the number. And here are some clues:
                When i say:     That means:
                Pico            One digit is correct but in the wrong position.
                Fermi           One digit is correct in the rigth position.
                Bagels          No digit is correct.
                """.format(NUM_DIGITS)
    )

    # main game loop
    while True:
        secret_num = get_secret_number()
        print("I have thought up a number")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}.".format(secret_num))

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break

    print("Thanks for playing!")


# functions
def get_secret_number():
    """Returns a string made up of NUM_DIGITS unique random digit"""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns string with pico, fermi, bagels clues for a guess and secret number pair"""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
