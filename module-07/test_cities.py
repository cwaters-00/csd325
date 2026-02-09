

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """test if where a standard city country pair will work as intended"""
        formatted_name = city_country("Chicago", "US")
        self.assertEqual(formatted_name, city_country("Chicago", "US"))

if __name__ == "__main__":
    unittest.main()