import random

answer = str(random.randint(100,1000))


def play_game():
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
    
    for num in range(1,11):
        clues = []
        print(f"Guess #{num}")
        guess = str(input("> "))

        for i in range(len(guess)):
            if guess == answer:
                print("You Got It!")
                play_again()
                break
            elif guess[i] == answer[i]:
                clues.append("Fermi")
            elif guess[i] in answer and guess[i] != answer[i]:
                clues.append("Pico")
        if len(clues) == 0:
            print("Bagels")

        clues.sort()
        print(" ".join(clues))
    

    print("You ran out guess.")
    print("The answer was {}".format(answer))

def play_again():
    print("")
    print("Do you want to play again? (yes or no)")
    reponse = input("> ")

    if reponse == "yes" or reponse == "Yes":
        play_game()
    else:
        print("Thanks for playing!")
        exit()
        

if __name__ == "__main__":
    play_game()


