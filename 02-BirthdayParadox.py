import random
import datetime

print("How many birthdays shall I Generate? (Max 100)")
num_birthdays = int(input("> "))

birthdays = set()

year = 2025

count = num_birthdays
for i in range(count):
    try:
        month = random.randrange(1,13)
        day = random.randrange(1,31)

        date = str(datetime.date(year,month,day))
        birthdays.add(date)
    except (ValueError):
        print(f"Skipping {date} due to ValueError")
        continue
    else:
        count -= 1
    finally:
        if count == birthdays:
            break
        else:
            continue


print(birthdays)
print(len(birthdays))



