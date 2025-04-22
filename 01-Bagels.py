import random

answer = random.randint(100,999)
print(answer)
clues =  []
for num in range(1,11):
    print(f"Guess #{num}:")
    guess = str(input("> "))
    if guess == clues:
        print("You got it!")

    for i in range(len(clues)):
        if guess[i] == clues[i]:
            clues.append('Fermi')
        elif guess[i] in clues:
            clues.append('Pico')
        print(clues)

        

    if len(clues) == 0:
        clues.append("Bagels")


