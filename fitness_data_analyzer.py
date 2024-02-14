def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    height_in_centimeters = height / 100
    body_mass_index = weight / height_in_centimeters ** 2
    return body_mass_index


def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    burned_calories_per_minute = 6.67
    estimated_burned_calories = burned_calories_per_minute * duration
    return estimated_burned_calories


def filter_underweight_people(people_data):
    """Filter underweight people based on BMI."""
    underweight_people = []

    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi <= 18.5:
            underweight_people.append(person)
    return underweight_people


def filter_normal_weight_people(people_data):
    """Filter normal_weight people based on BMI."""
    normal_weight_people = []

    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if 18.5 < bmi <= 24.9:
            normal_weight_people.append(person)
    return normal_weight_people


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []

    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if 24.9 < bmi <= 29.9:
            overweight_people.append(person)
    return overweight_people


def filter_obesity_people(people_data):
    """Filter obesity people based on BMI."""
    obesity_people = []

    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 30:
            obesity_people.append(person)
    return obesity_people


# Main program
people_data = []
counter = 0
print("\n---<< Enter fitness data for each person (Enter a blank name to finish):")
while True:
    if counter != 0:
        command = input("\n---<< For new analysis press [y] | else press any key for result/s and exiting the program: ")
        if command != "y":
            break

    name = input("---<< Enter person's name: ").strip()
    if not name:
        break

    weight = float(input("---<< Enter person's weight in kilograms: "))
    if weight < 0:
        weight = float(input("‼️---<< Invalid weight. Try again: "))
    height = float(input("---<< Enter person's height in meters: "))
    duration = float(input("---<< Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)
    counter += 1


print(f"\n{"---<< "}{78 * '-'}{" >>---"}")
print("---<< Fitness Analysis: 📋 >>---")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

underweight_people = filter_underweight_people(people_data)
normal_weight_people = filter_normal_weight_people(people_data)
overweight_people = filter_overweight_people(people_data)
obesity_people = filter_obesity_people(people_data)

if len(underweight_people) == 0:
    print("\n---<< Underweight People: n/a")
    print(f"{32 * '-'}\n")
else:
    print("\n---<< Underweight People:")
    for person in underweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(32 * '▼')
        print(f"❂ {person['name']}: BMI = {bmi:.2f}")
        print(f"{32 * '▲'}\n")

if len(normal_weight_people) == 0:
    print("---<< Normal Weight People: n/a")
    print(f"{32 * '-'}\n")
else:
    print("---<< Normal Weight People:")
    for person in normal_weight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(32 * '▼')
        print(f"❂ {person['name']}: BMI = {bmi:.2f}")
        print(f"{32 * '▲'}\n")

if len(overweight_people) == 0:
    print("---<< Overweight People: n/a")
    print(f"{32 * '-'}\n")
else:
    print("---<< Overweight People:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(32 * '▼')
        print(f"❂ {person['name']}: BMI = {bmi:.2f}")
        print(f"{32 * '▲'}\n")


if len(obesity_people) == 0:
    print("---<< Obesity People: n/a")
    print(f"{32 * '-'}\n")
else:
    print("---<< Obesity People:")
    for person in obesity_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(32 * '▼')
        print(f"❂ {person['name']}: BMI = {bmi:.2f}")
        print(f"{32 * '▲'}\n")
