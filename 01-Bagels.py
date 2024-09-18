# To-Do
# [x] - Varaibles for generating random 3 digital values
# [x] - A loop to only provide the user with 10 guesses
# [x] - a statement that printed bagel whenever all the values are incorrect
# [x] - make the clues into a list (Pico And Fermi) 
    # The Loop Should interate through the str one but one (For Loop)
# [x] - Exception Handling

import random

clues = []
ans = str(random.randrange(100,999))

def main():
    print("""
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
""")
    
    for chances in range(1,11):
        print(f"Guess #{chances}")
        guess = input("> ")

        for i in range(len(guess)):
            if guess[i] == ans[i]:
                # One Digit is correct and in the right position
                clues.append("Fermi")
            elif guess[i] in ans:
                # One digit is correct but in the incorrent position
                clues.append("Pico")

        if guess == ans:
            print("You got it!")
            end_game()
            break
        elif len(clues) == 0:
            clues.append("Bagels")
        
        print(*clues)
        clues.clear()


def end_game():
    print("Do you want to play again? (yes or no)")
    end_game = input("> ")
    if end_game == 'yes':
        main()
    elif end_game == 'no':
        exit()


if "__main__" == __name__:
    try:
        main()
        print("Actual Answer: ",ans)
    except Exception as e:
        print(f"An error occured: {e}")
