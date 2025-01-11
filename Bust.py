import random

Max_digits = 3
Max_guesses = 20

def main():
    print("""I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
    Mishap One digit is correct but in the wrong position.
    Spot On One digit is correct and in the right position.
    Bust No digit is correct.""".format(Max_digits))

    while True:
        secret_number = secret_num()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(Max_guesses))

        numguess = 1
        while numguess <= Max_guesses:
            guess = ''
            while len(guess) != Max_digits or not guess.isdecimal():
                print(f'Guess number: {numguess}')
                guess = input('>>> ')

                if len(guess) != Max_digits or not guess.isdecimal():
                    print(f"Invalid input. Please enter a {Max_digits}-digit number.")

            clue = getclue(guess, secret_number)
            print(f"Clue: {clue}")  # Show the clue

            if guess == secret_number:
                print("You got it!!!")
                break

            numguess += 1
            if numguess > Max_guesses:
                print("You ran out of guesses. Oops!")
                print(f"The number was {secret_number}")

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

        print("Thanks for playing!")


def secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''.join(numbers[:Max_digits])
    return secretNum


def getclue(guess, secretNum):
    if guess == secretNum:
        return 'You got it!!!'

    clue_array = []
    secretNum_copy = list(secretNum)


    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue_array.append('Spot On')

            secretNum_copy[i] = None


    for i in range(len(guess)):
        if guess[i] != secretNum[i] and guess[i] in secretNum_copy:
            clue_array.append('Mishap')
            secretNum_copy[secretNum_copy.index(guess[i])] = None

    if len(clue_array) == 0:
        return 'Bust'
    else:
        clue_array.sort()
        return ' '.join(clue_array)



if __name__ == "__main__":
    main()
