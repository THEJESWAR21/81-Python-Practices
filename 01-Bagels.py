import random

answer = str(random.randint(100,1000))
print(answer)

clues = []

INTRO = """
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
"""


def play_game():
    Win = False
    print(INTRO)
    for guess_count in range(1,11):
        
        print(f"Guess #{guess_count}")
        guess = input("> ")

        if answer == guess:
            print("YOU WON!!!")
            Win = True
            break
        
        else:
            for i in range(3):
                if (answer[i] == guess[i]):
                    clues.append("Fermi")
                    
                elif (answer[i] in guess):
                    clues.append("Pico")

        if not clues:
            print("Bagels")

        print(*clues)
        clues.clear()


    if Win == False:
        print("Guess chance exceded Try Again Later!")

    print("Thanks for playing!")

play_game()

while True:
    play = input("Do you want to play again? (y/n): ").strip().lower()
        
    if play == "y":
        print("Great! Let Start the game again")
        play_game()
    elif play == "n":
        print("Okay, maybe next time")
        exit()
    else:
        print("Please type y or n for YES OR NO")


# FIX KNOWLEDGE ON STR MANUPULATION
# REFRESH KNOWLEDGE ON LOOPS
# WHAT DOES *list_name DO
# LEARN MORE ABOUT LISTS
# Learn about local and global variable and how to access them in difference scenario