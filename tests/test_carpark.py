import unittest
from src.carpark import Carpark
from src.carpark import Car
from src.display import Display


class TestCarPark(unittest.TestCase):
      def setUp(self):
         self.car_park = Carpark(100, "123 Example Street", [Display("Display1"), Display("Display2")])

      def test_car_park_initialized_with_all_attributes(self):
         self.assertIsInstance(self.car_park, Carpark)
         self.assertEqual(self.car_park.location, "123 Example Street")
         self.assertEqual(self.car_park.bays, 100)
         self.assertEqual(self.car_park.displays, [Display.get_display("Display1"), Display.get_display("Display2")])
         self.assertEqual(self.car_park.get_available_bays(), 100)

      def test_add_car(self):
         self.car_park.add_car(Car("FAKE-001"))
         self.assertEqual(self.car_park.get_available_bays(), 99)

      def test_remove_car(self):
         car = Car("FAKE-001")
         self.car_park.add_car(car)
         self.car_park.remove_car(car)
         self.assertEqual(self.car_park.get_available_bays(), 100)

      def test_overfill_the_car_park(self):
         for i in range(100):
            self.car_park.add_car(Car(f"FAKE-{i}"))
         self.assertEqual(self.car_park.get_available_bays(), 0)
         self.car_park.add_car(Car("FAKE-100"))
         # Overfilling the car park should not change the number of available bays
         self.assertEqual(self.car_park.get_available_bays(), 0)

         # Removing a car from an overfilled car park should not change the number of available bays
         with self.assertRaises(ValueError):
             self.car_park.remove_car(Car("FAKE-100"))
         self.assertEqual(self.car_park.get_available_bays(), 0)

      def test_removing_a_car_that_does_not_exist(self):
         with self.assertRaises(ValueError):
            self.car_park.remove_car(Car("NO-1"))


if __name__ == "__main__":
   unittest.main()