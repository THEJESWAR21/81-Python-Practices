import random, datetime


def get_birthdays():
    # Generating a random day from the year
    random_day = random.randint(1,365)

    start_date = datetime.date(2024,1,1)

    # incrimenting the start_date by the random_day to get a random date
    # random_day - 1 because if not day 1 == Jan 02 because of the starting date
    random_date = start_date + datetime.timedelta(days=random_day - 1)

    # Turns the month number to a string and concatenates it with the day
    birthday = random_date.strftime('%b') + " " + str(random_date.day)

    return birthday

def get_match():
    birthdays = []
    for _ in range(n):
        birthdays.append(get_birthdays())
    if len(birthdays) == len(set(birthdays)):
        return None
    else:
        # For every item in brithday_A the item after the first interate through to check whether that item exists or not
        for a, birthday_A in enumerate(birthdays):
            for b, birthday_B in enumerate(birthdays[a+1:]):
                if birthday_A == birthday_B:
                    return birthday_A
                

while True:
    try:
        print("Birthday Paradox, by AI Sweigart al@inventwithpython.com")
        print("How many birthday shall i generate (Max 100)")
        n = int(input('> '))
    except Exception as e:
        print(f"Error:{e}")
    else:
        break

        
if get_match():
    print(f"In This Simulation multiple people have a birthday on {get_match()}")
elif get_match() == None:
    print(f"In This Simultation no one has the same birthday")


match_found = 0
print("Generating 23 random birthdays 100,000 times...")
input("Press enter to begin...")
print("Lets run a another 100,000 simulation")

simulations = 100_000

for i in range(simulations):
    if i % 10000 == 0:
        print(i, 'simulation run...') 

    if get_match() != None:
        match_found += 1  # Increment if a match is found

print("100,000 simulations run.")

percentage = (match_found / simulations) * 100

print(
    f"""
Out of 100,000 simulations of {n} people, there was a
matching birthday in that group {match_found} times. This means
that {n} people have a {percentage % round(percentage,2)} % chance of
having a matching birthday in their group.
That's probably more that you would think! 
    """
    )