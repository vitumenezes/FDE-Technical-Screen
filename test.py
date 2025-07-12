import unittest
from main import sort

class TestSort(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_special_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")  # 1,000,000 cm³

    def test_special_bulky_by_dimension(self):
        self.assertEqual(sort(160, 30, 30, 5), "SPECIAL")  # width >= 150

    def test_special_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")  # heavy only

    def test_rejected_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_edge_volume_just_below_limit(self):
        self.assertEqual(sort(99, 100, 100, 10), "STANDARD")  # 990,000 cm³

    def test_edge_mass_just_below_limit(self):
        self.assertEqual(sort(50, 50, 50, 19.9), "STANDARD")

    def test_invalid_dimension_zero(self):
        with self.assertRaises(ValueError):
            sort(0, 100, 100, 10)

    def test_invalid_negative_dimension(self):
        with self.assertRaises(ValueError):
            sort(-10, 50, 50, 10)

    def test_invalid_negative_mass(self):
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -1)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            sort("100", 50, 50, 10)

if __name__ == "__main__":
    unittest.main()
