import random

# To-Do
# [ ] - Game Menu
# [x] - Varaibles for generating random 3 digital values
# [ ] - A For Loop To provide an input whenever the userinput is false
# [ ] - Function that check user input with the answer and provide an output
# [ ] - Error Handling

ans = tuple(str(random.randrange(100,999)))
print(ans)

clues = ""

for chances in range(1,11):
    print(f"Guess #{chances}")
    guess = tuple(input(" > "))
    if ans == guess:
        break
    else:
        for ans_ind, ans_val in enumerate(ans):
            for guess_ind, guess_val in enumerate(guess):
                if ans_val == guess_val and ans_ind != ans_val:
                    clues = "Pico"
                    print(clues)
                elif ans_val == guess_val and ans_ind == ans_val:
                    clues = "Fermi"
                    print(clues)
                elif ans_val != guess_val and ans_ind != ans_val:
                    clues = "Bagel"
                    print(clues)
