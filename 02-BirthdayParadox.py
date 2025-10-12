import random
import datetime
import statistics

print("How Many Birthdays Shall I Generate? (Max 100)")
user_days = int(input("> "))

# Default Year
year = 2025
birthdays = []

## Generates Random Days In an Year and put it in a list
def generate_birthdays():
    birthdays.clear()
    start_date = datetime.date(year,1,1)
    end_date = datetime.date(year,12,31)

    days_between = (end_date - start_date).days
    
    for _ in range(user_days):
        random_day = random.randint(start_date.day, days_between) # 1 - 364 is the range
        random_date = start_date + datetime.timedelta(days=random_day)

        birthdays.append(str(random_date.strftime("%b") + " " + str(random_date.day)))


## Finds the duplicates in the list
def finding_duplicates():
    # Unique_birthdays = set(birthdays)
    duplicates = set()
    for i in birthdays:
        if birthdays.count(i) > 1:
            duplicates.add(i)
    return len(duplicates)

# Runs the programe 100,000 to find the probablity 
def simualtions():
    total_duplicate_count = 0

    print(f"Generating {user_days} random birthdays 100,000 times...")
    input("Let's run another 100,000 simulations.")
    for i in range(100_001):
        generate_birthdays()
        if len(set(birthdays)) < len(birthdays):
            total_duplicate_count += 1

        if (i % 10_000 == 0 or i == 100_000):
            print(f"{i} simulation run...")

    probability = round((total_duplicate_count / 100_000) * 100, 2)
    print(f"Out of 100,000 simulations of {user_days} people, there was a matching birthday in that group {total_duplicate_count} times. This means")
    print(f"that {user_days} people have a {probability}% chance of having a matching birthday in their group. That's probably more than you would think!")
    return total_duplicate_count

# The Main program that handles and exetures the functions 
def main():
    generate_birthdays()

    print(f"Here are {user_days} Birthdays: ")
    print(", ".join(birthdays))

    if finding_duplicates:
        duplicates_mode = statistics.mode(birthdays)
        print(f"\nIn this simulation, multiple people have a birthday on {duplicates_mode}")
    else:
        print("\nNo shared birthdays found in this simulation!") 
    
    simualtions()

main()

# Learn Functional Programming