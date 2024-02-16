import unittest


def calculate_bmi(weight, height):
    height_in_centimeters = height / 100
    body_mass_index = weight / height_in_centimeters ** 2
    return body_mass_index


class TestCalculateBmi(unittest.TestCase):
    def test_bmi_with_high_weight_and_height(self):

        message = "the result is not correct"
        self.assertEqual(calculate_bmi(95, 181,), 28.997893837184456, message)

    def test_bmi_with_low_weight_and_height(self):
        message = "the result is not correct"
        self.assertEqual(calculate_bmi(50, 100), 50, message)




def calculate_calories_burned(duration):
    burned_calories_per_minute = 6.67
    estimated_burned_calories = burned_calories_per_minute * duration
    return estimated_burned_calories


class TestCalculateCaloriesBurned(unittest.TestCase):
    def test_low_calories_burned(self):

        message = "the result is not correct"
        self.assertEqual(calculate_calories_burned(20), 133.4, message)

    def test_high_calories_burned(self):

        message = "the result is not correct"
        self.assertEqual(calculate_calories_burned(100), 667, message)




if __name__ == '__main__':
    unittest.main()
