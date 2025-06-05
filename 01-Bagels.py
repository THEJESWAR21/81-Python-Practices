import random

secretNum = str(random.randrange(100,1000))
numDigit = 3

def header():
    print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.""")

print(secretNum)
def main():
    clues = []
    for count in range(1,11):
        print("")
        print(f"Guess #{count}")
        guess = input("> ")

        if guess == secretNum:
            print("You Won")
            break
        elif guess.isdigit() == False:
            print("Only Enter in a Number")
            continue
        elif len(guess) > 3 or len(guess) < 3:
            print("Enter only a 3 digit value, Try Again!")
            continue
        else:
            for i in range(len(guess)):
                if guess[i] == secretNum[i]:
                    clues.append("Fermi")
                elif guess[i] in secretNum:
                    clues.append("Pico")
        
        if len(clues) == 0:
            print("Bagels")
        else:
            clues.sort()
            print(*clues)
        
        clues.clear()

header()
main()

print("You are out of tries try again later")