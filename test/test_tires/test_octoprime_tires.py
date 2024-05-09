import unittest
import numpy as np
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [0.9, 0.7, 0.8, 0.5]

        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.9, 0.7, 0.8, 0.3]

        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()