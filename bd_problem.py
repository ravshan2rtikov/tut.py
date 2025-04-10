import math
import datetime, random


def get_birthdays(number_of_birthdays):
    # returns a random list of number random date objects for bdays
    birthdays = []

    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        bday = start_of_year + random_number_of_days
        birthdays.append(bday)
    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a


print("""Birthday paradox shows us that in a group of N people, the odds that two of them
      have matching birthdays is surprisingly large.
      This Program does a Monte carlo simulation (that is, repeated random simulations) 
      to explore this concept.

     (it is not a paradox, it is just a surpriising result.)""")

# set a tuple of month names in order
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True:
    print("How many birthdays shall i generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_birhtdays = int(response)
        break
print()

# generate and display birthdays
print("Here are", num_birhtdays, "birthdays: ")
birthdays = get_birthdays(num_birhtdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")

    month_name = MONTHS[birthday.month - 1]
    date_text = "{} {}".format(month_name, birthday.day)
    print(date_text, end="")
print()
print()

# determine if there are matching bdays
match = get_match(birthdays)

print("In this simulattion, ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = "{} {}".format(month_name, match.day)
    print("multiple people have a birthday on", date_text)
else:
    print("there are no matching birthdays")
print()

# run through 100,000 simulations
print("Generating", num_birhtdays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations")
sim_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = get_birthdays(num_birhtdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# display simulations result
probability = round(sim_match / 100_000 * 100, 2)
print("out of 100,000 simulations of", num_birhtdays, "people, there was a")
print("matching birthdays in that group", sim_match, "times. This means")
print("that", num_birhtdays, "people have a", probability, "% chance of")
print("having a matching birthday in their group")
print("That's probably more than you would think!")
