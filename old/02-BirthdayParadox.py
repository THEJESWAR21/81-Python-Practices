import random, datetime

class Birthday:
    def __init__(self) -> None:
        self.date = self.generate_birthdays()
    
    def generate_birthdays(self):
         # Generating a random day from the year
        random_day = random.randint(1,365)
        start_date = datetime.date(2024,1,1)
        # incrimenting the start_date by the random_day to get a random date
        # random_day - 1 because if not day 1 == Jan 02 because of the starting date
        random_date = start_date + datetime.timedelta(days=random_day - 1)
        return random_date.strftime('%b') + " " + str(random_date.day)
 
 
class BirthdaySimulation:
    def __init__(self, num_people):
        self.num_people = num_people
        self.birthdays = []

    def generate_birthday(self):
        self.birthdays = [Birthday().date for _ in range(self.num_people)]
    
    def get_match(self):
        self.generate_birthday()
        if len(self.birthdays) == len(set(self.birthdays)):
            return None
        else:
            # For every item in brithday_A the item after the first interate through to check whether that item exists or not
            for a, birthday_A in enumerate(self.birthdays):
                for b, birthday_B in enumerate(self.birthdays[a + 1:]):
                    if birthday_A == birthday_B:
                        return birthday_A
                    
    def run_simulation(self, num_simulations=100_000):
        match_found = 0
        print("Generating", self.num_people, "random birthdays", num_simulations, "times...")
        input("Press enter to begin...")

        for i in range(num_simulations):
            if i % 10000 == 0:
                print(i,"Simulation run....")
            
            if self.get_match() is not None:
                match_found += 1

        print(f"{num_simulations} simulations run.")
        print("100,000 simulations run.")

        percentage = (match_found / num_simulations) * 100

        print(f"""
Out of 100,000 simulations of {self.num_people} people, there was a
matching birthday in that group {match_found} times. This means
that {self.num_people} people have a {round(percentage, 2)} % chance of
having a matching birthday in their group.
That's probably more that you would think! 
""")


def main():
    while True:
        try:
            print("Birthday Paradox, by AI Sweigart al@inventwithpython.com")
            print("How many birthdays shall I generate? (Max 100)")
            num_people = int(input('> '))
            if num_people > 100 or num_people <= 0:
                raise ValueError("Number of people must be between 1 and 100.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            break

    simulation = BirthdaySimulation(num_people)

    if simulation.get_match():
        print(f"In this simulation, multiple people have a birthday on {simulation.get_match()}")
    else:
        print("In this simulation, no one has the same birthday.")

    simulation.run_simulation()

if __name__ == "__main__":
    main()
