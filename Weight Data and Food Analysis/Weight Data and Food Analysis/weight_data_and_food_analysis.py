import requests


def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    body_mass_index = weight / height ** 2
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



def name_validity_check(name):
    """Check if name is valid."""
    try:
        if name.isalpha():
            return True
        else:
            return False
    except AttributeError:
        return False


def weight_validity_check(weight):
    """Check if weight is valid and if is in the range [1, 200]."""
    try:
        if 0 < weight <= 200:
            return True
        else:
            return False
    except AttributeError:
        return False


def height_validity_check(height):
    """Check if height is valid and if is in range 1, 250  in centimeters"""
    try:
        if 0 < height <= 2.50:
            return True
        else:
            return False
    except AttributeError:
        return False


def duration_validity_check(duration):
    """Check if duration is valid and if is in the range 1, 120  in minutes"""
    try:
        if 0 <= duration <= 120:
            return True
        else:
            return False
    except AttributeError:
        return False


# Main program

def main_program():
    """

    This is the Main program.
    From here it collects information from the user,
    connects to the rest of the functions,
    and prints the output as a final step

    """

    people_data = []

    print("\n---<< Fitness data analyst and recipe generator for each person (Enter a blank name to finish) >>---")
    while True:
        command = input("\n---<< You have 3 options:"
                        "\n---<❂ For new analysis press [y] |"
                        "\n---<❂ For generating food recipes press [f] |"
                        "\n---<❂ For result/s and exiting the program type [quit] |"
                        "\n---<< If you continue with analysis you can choose anything else after the cycle !")

        if command == "quit":
            break

        elif command == "y":
            name = input("---<< Enter person's name: ").strip()
            while not name_validity_check(name):
                name = input("‼️---<< Enter valid name using only letters: ").strip()

            weight = float(input("---<< Enter person's weight in kilograms: "))
            while not weight_validity_check(weight):
                weight = float(input("‼️---<< Invalid weight. Try again[1, 200 kg]: "))

            height = float(input("---<< Enter person's height in meters: "))
            while not height_validity_check(height):
                print("‼️---<< Invalid height. Example: If you are 170 cm tall --> type 1.70")
                height = float(input("---<< Try again[1, 2.50 m]: "))

            duration = float(input("---<< Enter exercise duration in minutes: "))
            while not duration_validity_check(duration):
                duration = float(input("‼️---<< Invalid duration. Try again[0, 120 min]: "))

            person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
            people_data.append(person)


        elif command == "f":
            api_key = "5f5f599ca7a74124802636d26a9a7a9f"

            def get_recipe_by_url(title, recipe_id):
                slug = title.lower().replace(" ", "-")
                return f"https://spoonacular.com/recipes/{slug}-{recipe_id}"

            url = "https://api.spoonacular.com/recipes/complexSearch"
            query = input("\n---<< Enter the name of a meal to start search: \n")
            parameters = {
                "query": query,
                "number": 5,
                "apiKey": api_key
            }

            response = requests.get(url, params=parameters)

            if response.status_code == 200:
                data = response.json()
                if data.get("results"):
                    print(f"\n---<< Here are the top 5 results with keyword [ {query} ]:")
                    for result in data["results"]:
                        title = result["title"]
                        recipe_id = result["id"]
                        link = get_recipe_by_url(title, recipe_id)
                        print(f"Title: {title}\nLink: {link}\n")
                else:
                    print(f"‼️---<< The [ {query} ] is not included or is not spelled correctly.")
            else:
                print(f"‼️---<< Failed. Status code: {response.status_code} ")


    print(f"\n{'---<< '}{78 * '-'}{' >>---'}")
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




if __name__ == "__main__":
    main_program()
