from django.test import TestCase
from bikes.models import Bike

# Create your tests here.

class BikeTests(TestCase):
    def test_str(self):
        test_name = Bike(name="pass")
        self.assertEqual(str(test_name), "pass")