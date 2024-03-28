import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase): 
    
    def test_city_country(self):
        location = get_city_country("santiago", "chile")
        self.assertEqual(location,"Santiago, Chile")

    def test_city_country_population(self):
        population = get_city_country("santiago", "chile", 5000000)
        self.assertEqual(population,"Santiago, Chile – População 5000000")

unittest.main()