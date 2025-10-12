import random
import datetime

print("How Many Birthdays Shall I Generate? (MAX 100)")
user_days = int(input("> "))

year = 2025

birthdays = []
birthdays_set = set()


def generate_birthdays():
    start_date = datetime.date(year,1,1)
    end_date = datetime.date(year,12,31)

    days_between = (end_date - start_date).days
    
    for i in range(user_days):
        random_day = random.randint(start_date.day, days_between) # 1 - 364 is the range
        random_date = start_date + datetime.timedelta(days=random_day)

        birthdays.append(str(random_date.strftime("%b") + " " + str(random_date.day)))
        birthdays_set.add(str(random_date.strftime("%b") + " " + str(random_date.day)))

def same_birthday():
    commonality = list(set(birthdays) ^ birthdays_set)
    commonality_num = len(birthdays) - len(birthdays_set)

    print(commonality)
    print(commonality_num)


def main():
    generate_birthdays()

    print("Here are 23 Birthdays: ")
    same_birthday()



main()


