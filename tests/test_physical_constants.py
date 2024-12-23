import unittest
from constants.physical_constants import PhysicalConstants

class TestPhysicalConstants(unittest.TestCase):
    def test_speed_of_light(self):
        self.assertEqual(PhysicalConstants.SPEED_OF_LIGHT, 299_792_458)

    def test_gravitational_constant(self):
        self.assertAlmostEqual(PhysicalConstants.GRAVITATIONAL_CONSTANT, 6.67430e-11)

if __name__ == "__main__":
    unittest.main()
