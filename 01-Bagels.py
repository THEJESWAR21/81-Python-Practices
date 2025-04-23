import random

numDigits = 3
secretNum = str(701)
print(secretNum)

print(
'''Bagels, a deductive logic game.
 By Al Sweigart al@inventwithpython.com
  
 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
  
 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.'''.format(numDigits))

for num in range(1,11):
    print(f"Guess #{num}:")
    guess = str(input("> "))

    try:
        clues = []
        for i in range(len(secretNum)):
            if guess[i] == secretNum[i]:
                clues.append("Fermi")
            elif guess[i] in secretNum:
                clues.append("Pico")
    
        print(*clues)
        if guess == secretNum:
            print("You got it!")
            break
        elif num == 10:
            print(f"You Loss The Secret Number is {secretNum}")
            print("Thanks For Planning")
    except Exception as e:
        print("Error Try Again!")
        break

    if len(clues) == 0:
        clues.append("Bagels")
    else:
        clues.sort()

