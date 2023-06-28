import unittest
from models.attraction import Attraction

class TestAttraction(unittest.TestCase):
    def setUp(self):
        self.attraction1 = Attraction('Amstel Bridge', 'Amsterdam', 'amazing view into the heart of the city')
        self.attraction2 = Attraction('Royal Ontario Museum', 'Toronto', 'recommend it highly the World exhibit is fantastic!')

    def test_attraction1_has_name(self):
        self.assertEqual('Amstel Bridge', self.attraction1.name)

    def test_attraction1_has_city(self):
        self.assertEqual('Amsterdam', self.attraction1.city)

    def test_attraction1_has_review(self):
        self.assertEqual('amazing view into the heart of the city', self.attraction1.review)

    def test_attraction2_has_name(self):
        self.assertEqual('Royal Ontario Museum', self.attraction2.name)

    def test_attraction2_has_city(self):
        self.assertEqual('Toronto', self.attraction2.city)

    def test_attraction2_has_review(self):
        self.assertEqual('recommend it highly the World exhibit is fantastic!', self.attraction2.review)
    
