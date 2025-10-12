import random
import datetime
import statistics

print("How Many Birthdays Shall I Generate? (MAX 100)")
user_days = int(input("> "))

year = 2025
birthdays = []

def generate_birthdays():
    birthdays.clear()
    start_date = datetime.date(year,1,1)
    end_date = datetime.date(year,12,31)

    days_between = (end_date - start_date).days
    
    for _ in range(user_days):
        random_day = random.randint(start_date.day, days_between) # 1 - 364 is the range
        random_date = start_date + datetime.timedelta(days=random_day)

        birthdays.append(str(random_date.strftime("%b") + " " + str(random_date.day)))

def finding_duplicates():
    # Unique_birthdays = set(birthdays)
    duplicates = set()
    for i in birthdays:
        if birthdays.count(i) > 1:
            duplicates.add(i)
    return len(duplicates)

def simualtions():
    total_duplicate_count = 0
    for i in range(100_001):
        generate_birthdays()
        count = finding_duplicates()
        total_duplicate_count += count

        if (i % 10_000 == 0 or i == 100_000):
            print(f"{i} simulation run...")

    percentage = (total_duplicate_count / 100_000) * 100
    print(f"Out of 100,000 simulations of {user_days} people, there was a matching birthday in that group {total_duplicate_count} times. This means""")
    print(f"{percentage}")
    return total_duplicate_count
        
def main():
    generate_birthdays()

    print(f"Here are {user_days} Birthdays: ")
    print(", ".join(birthdays))

    if finding_duplicates:
        duplicates_mode = statistics.mode(birthdays)
        print(f"\nIn this simulation, multiple people have a birthday on {duplicates_mode}")
    else:
        print("\nNo shared birthdays found in this simulation!") 

    count = finding_duplicates()
    
    simualtions()

main()