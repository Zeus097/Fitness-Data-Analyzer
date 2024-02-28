import unittest


def main_program():

    """"
    Testing the functionality of the list( people_data ) from main_program function.
    """

    people_data = []
    counter = 0
    print("\n---<< Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        if counter != 0:
            command = input(
                "\n---<< For new analysis press [y] | else press any key for result/s and exiting the program: ")
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
        return people_data



class TestMainProgram(unittest.TestCase):
    def test_people_data(self):

        expect = [{'duration': 60.0, 'height': 2.00, 'name': 'Zeus', 'weight': 90.0}]
        message = "people_data is not correct !"
        self.assertEqual(main_program(), expect, message)





if __name__ == '__main__':
    unittest.main()
