# To-Do
# [x] - Varaibles for generating random 3 digital values
# [x] - A loop to only provide the user with 10 guesses
# [x] - a statement that printed bagel whenever all the values are incorrect
# [ ] - make the clues into a list (Pico And Fermi) 
    # The Loop Should interate through the str one but one (For Loop)
# [ ] - Exception Handling

import random

clues = []

# ans = str(random.randrange(100,999))
ans = "701"
print(ans)

for chances in range(1,11):
    print(f"Guess #{chances}")
    guess = input(">>>> ")

    for i in range(len(guess)):
        if guess[i] == ans[i]:
            # One Digit is correct and in the right position
            clues.append("Fermi")
        elif guess[i] in ans:
            # One digit is correct but in the incorrent position
            clues.append("Pico")

    if guess == ans:
        print("You Won!")
        break
    elif len(clues) == 0:
        clues.append("Bagels")
    
    print(*clues)
    clues.clear()