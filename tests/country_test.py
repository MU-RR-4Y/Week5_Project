import unittest
from models.country import Country
from models.destination import Destination

class TestCountry (unittest.TestCase):
    def setUp(self):
        self.destination_1 = Destination('Rome', 'Capital of Italy')
        self.country =Country('Italy')
        

    def test_country_name(self):
        self.assertEqual('Italy', self.country.name)

    def test_country_destination(self):
        self.assertEqual(0, len(self.country.destination))

    def test_adding_destination(self):
        self.country.add_destination(self.destination_1)
        self.assertEqual(1, len(self.country.destination))
        self.assertEqual('Rome', self.country.destination[0].name)

    def test_country_id__isNone(self):
        self.assertIsNone(self.country.id)
   
    def test_country_isNotNone(self):
        self.country.id = 1
        self.assertEqual(1, self.country.id)