import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country1 = Country('France')
        self.country2 = Country('Canada')
        self.country3 = Country('Netherlands')
        self.country4 = Country('Greece')

    def test_country1_has_name(self):
        self.assertEqual('France', self.country1.name)

    def test_country2_has_name(self):
        self.assertEqual('Canada', self.country2.name)

    def test_country3_has_name(self):
        self.assertEqual('Netherlands', self.country3.name)

    def test_country4_has_name(self):
        self.assertEqual('Greece', self.country4.name)