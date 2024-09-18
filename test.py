import random

ans = str(random.randrange(100,999))
print(tuple(ans))
guess =  str(random.randrange(100,999))
print(tuple(guess))


for ans_index, ans_value in enumerate(ans):
    for guess_index, guess_value in enumerate(guess):
        if ans_value == guess_value:
            print(f"Match Found: {ans_value} at index {ans_index} in tuple1 and index {guess_index} in tuple2")
        else:
            print("No Match Found")
