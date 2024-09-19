import datetime, random


def random_date():
    # Generate a random day somewhere in a year
    random_day = random.randint(1, 365)

    start_date = datetime.date(2024,1,1)

    # Add the progressing days data to the start_date to update it
    # random_day - 1 because if not day 1 == Jan 02 because of the starting date
    random_date = start_date + datetime.timedelta(days=random_day - 1)

    month = random_date.strftime('%b') # Turn the month number into a string 
    day = random_date.day

    return month,day

