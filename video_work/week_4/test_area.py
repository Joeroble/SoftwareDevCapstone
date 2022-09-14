from unittest import TestCase
import unittest
import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        # A triangle with height 4 and base 5 should have area 10
        self.assertEqual(10, area.triangle_area(4,5))

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    
if __name__ == '__main__':
    unittest.main()