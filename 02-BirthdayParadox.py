import random, datetime

birthdays = []

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


while True:
    try:
        print("How many birthday shall i generate (Max 100)")
        n = int(input('> '))
    except Exception as e:
        print(f"Error:{e}")
    else:
        break


duplicate = []


def get_match():
    for x in range(n):
        birthdays.append(get_birthdays())

    if len(birthdays) == len(set(birthdays)):
        return None
    else:
        # For every item in brithday_A the item after the first interate through to check whether that item exists or not
        for a, birthday_A in enumerate(birthdays):
            for b, birthday_B in enumerate(birthdays[a+1: ]):
                if birthday_A == birthday_B:
                    duplicate.append(birthday_A)
                    return birthday_A

print(get_match())
print(duplicate)
