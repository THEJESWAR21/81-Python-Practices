import random


answer = str(random.randint(100,1000))
print(answer)



def play_game():
    for num in range(1,11):
        clues = []
        print(f"Guess #{num}")
        guess = str(input("> "))

        for i in range(len(guess)):
            if guess == answer:
                print("You Got It!")
                break
            elif guess[i] == answer[i]:
                clues.append("Fermi")
            elif guess[i] in answer and guess[i] != answer[i]:
                clues.append("Pico")
            elif guess[i] not in answer:
                clues.append("Bagels")
                
    print(" ".join(clues))

print("You ran out guess.")
print("The answer was {}".format(answer))

def play_again():
    print("Do you want to play again? (yes or no)")
    reponse = input("> ")

    if reponse == "yes" or reponse == "Yes":
        play_again()
    else:
        print("Thanks for playing!")
        exit()
        


play_game()
play_again()


