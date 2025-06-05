import random
import calendar
import statistics


def calculate_date(num):
    dates = []
    for _ in range(num):
        month_index = random.randint(1,12)
        month_days = calendar.monthrange(2023, month_index)[1]
        month = calendar.month_abbr[month_index] # need to slice the list as [1]
        days = random.randint(1, month_days)

        date = f"{month} {days}"
        dates.append(date)
    return dates

print('How many birthdays shall I generate? (Max 100)')
num = int(input("> "))

dates = calculate_date(num)
print(f'Here are {num} birthdays:')
print(*dates, sep=', ')

try:
    most_common = statistics.mode(dates)
    print(f"In this simulation, multiple people have a birthday on {most_common}")
except statistics.StatisticsError:
    print("No unique most common birthday in this sample.")

print("\nLet's run another 100,000 simulations.")
print("0 simulations run...")

simulations = 0
total_matches = 0
input("Press Any Key to Start Simulation...")
while simulations < 100_000:
    dates = calculate_date(num) # Calling the Function

    if len(set(dates)) < len(dates):
        total_matches += 1
    simulations += 1


    if simulations == 10_000:
        print("10000 simulations run...")
    if simulations == 50_000:
        print("50000 simulations run...")
    if simulations == 90_000:
        print("90000 simulations run...")


probability = round(total_matches / 100_000 * 100, 2) 

print("100000 simulations run.")
print(f"""
      Out of 100,000 simulations of {num}, there was a
      matching birthday in that group {total_matches} times. This means
      that {num} people have a {probability} % chance of having a matching
      birthday in their group. 

      That's probably more than you would
      
      """
      )