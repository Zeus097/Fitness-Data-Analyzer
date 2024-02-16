import unittest
from TestCalculating import calculate_bmi


def filter_underweight_people(people_data):

    """
    Testing the functionality of filter_underweight_people.
    """

    underweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi <= 18.5:
            underweight_people.append(person)
    return underweight_people


class TestFilterUnderweightPeople(unittest.TestCase):
    def test_underweight_people(self):
        example = [{"duration": 20.0, "height": 180.0, "name": "John", "weight": 30.0}]
        expected = [{"duration": 20.0, "height": 180.0, "name": "John", "weight": 30.0}]
        message = "Not in bmi range"
        self.assertEqual(filter_underweight_people(example), expected, message)





def filter_normal_weight_people(people_data):

    """
    Testing the functionality of filter_normal_weight_people.
    """

    normal_weight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi <= 18.5:
            normal_weight_people.append(person)
    return normal_weight_people


class TestFilterNormalWeightPeople(unittest.TestCase):
    def test_normal_weight_people(self):

        example = [{"duration": 40.0, "height": 170.0, "name": "John", "weight": 50.0}]
        expected = [{"duration": 40.0, "height": 170.0, "name": "John", "weight": 50.0}]
        message = "Not in bmi range"
        self.assertEqual(filter_normal_weight_people(example), expected, message)





def filter_overweight_people(people_data):

    """
    Testing the functionality of filter_overweight_people.
    """

    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if 24.9 < bmi <= 29.9:
            overweight_people.append(person)
    return overweight_people


class TestFilterOverWeightPeople(unittest.TestCase):
    def test_overweight_people(self):

        example = [{"duration": 20.0, "height": 190.0, "name": "John", "weight": 100.0}]
        expected = [{"duration": 20.0, "height": 190.0, "name": "John", "weight": 100.0}]
        message = "Not in bmi range"
        self.assertEqual(filter_overweight_people(example), expected, message)





def filter_obesity_people(people_data):

    """
    Testing the functionality of filter_obesity_people.
    """

    obesity_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 30:
            obesity_people.append(person)
    return obesity_people


class TestFilterObesityPeople(unittest.TestCase):
    def test_obesity_people(self):

        example = [{"duration": 20.0, "height": 190.0, "name": "John", "weight": 150.0}]
        expected = [{"duration": 20.0, "height": 190.0, "name": "John", "weight": 150.0}]
        message = "Not in bmi range"
        self.assertEqual(filter_obesity_people(example), expected, message)



if __name__ == '__main__':
    unittest.main()
