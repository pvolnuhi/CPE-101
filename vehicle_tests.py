import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self):
        # Add code here.
        v = vehicle.Vehicle(4, 100, 4, True)
        self.assertEqual(v.wheels, 4)
        self.assertEqual(v.fuel, 100)
        self.assertEqual(v.doors, 4)
        self.assertEqual(v.roof, True)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()