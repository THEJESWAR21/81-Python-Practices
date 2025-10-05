import random
import calendar
import statistics


class BirthdayParadox:
    def __init__(self, year=2023):
        self.year = year
        self.dates = []


    def generate_birthdays(self, group_size):
        self.dates = []
        for _ in range(group_size):
            month_index = random.randint(1,12)
            month_days = calendar.monthrange(self.year, month_index)[1]
            day = random.randint(1, month_days)
            month = calendar.month_abbr[month_index]
            self.dates.append(f"{month} {day}")
        return self.dates
    
    def display_birthdays(self):
        print(f'Here are {len(self.dates)} birthdays:')
        print(",".join(self.dates))

    def find_most_common_birthday(self):
        try:
            most_common = statistics.mode(self.dates)
            print(f"In this simulation, multiple people have a birthday on {most_common}")
        except statistics.StatisticsError:
            print("No unique most common birthday in this sample.")
    
    def run_simulations(self, group_size, num_simulations=100_000):
        print("\nLet's run another 100,000 simulations.")
        print("0 simulations run...")
        total_matches = 0

        for simulation in range(1, num_simulations + 1):
            birthdays = self.generate_birthdays(group_size)
            if len(set(birthdays)) < len(birthdays):
                total_matches += 1

            if simulation in [10_000, 50_000, 90_000]:
                print(f'{simulation} simulations run...')

        probability = round(total_matches / num_simulations * 100, 2)
        print("100000 simulations run.")
        print(f"""
      Out of 100,000 simulations of {group_size} people, there was a
      matching birthday in that group {total_matches} times. This means
      that {group_size} people have a {probability}% chance of having a matching
      birthday in their group. 

      That's probably more than you would expect!
      """)
    
def main():
    print('How many birthdays shall I generate? (Max 100)')
    group_size = int(input("> "))

    simulator = BirthdayParadox()
    simulator.generate_birthdays(group_size)
    simulator.display_birthdays()
    simulator.find_most_common_birthday()

    input("Press Any Key to Start Simulation...")
    simulator.run_simulations(group_size)


if __name__ == "__main__":
    main()

