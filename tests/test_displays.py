import unittest
from src.display import Display
from src.carpark import Carpark


class TestDisplays(unittest.TestCase):

    def setUp(self):
        self.display = Display(1)
        self.car_park = Carpark(100, "123 Street", [self.display])

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "")

    def test_update(self):
        self.display.update_display("Goodbye")
        self.assertEqual(self.display.message, "Goodbye")

