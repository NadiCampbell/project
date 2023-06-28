import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city1 = City('Paris', 'France')
        self.city2 = City('Rotterdam', 'Netherlands')
        self.city3 = City('Toronto', 'Canada')

    def test_city1_has_name(self):
        self.assertEqual('Paris', self.city1.name)
    
    def test_city1_has_country(self):
        self.assertEqual('France', self.city1.country)

    def test_city2_has_name(self):
        self.assertEqual('Rotterdam', self.city2.name)

    def test_city2_has_country(self):
        self.assertEqual('Netherlands', self.city2.country)
