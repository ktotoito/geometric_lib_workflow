import unittest
from triangle import *


class GeometryTestTriangleValidArea(unittest.TestCase):
    def test_triangle_area_valid_value_right_triangle(self):
        self.assertEqual(area(13, 12, 5), 30.0)

    def test_triangle_area_valid_value_irregular_triangle(self):
        self.assertAlmostEqual(area(12,9, 8), 35.9991, 4)

    def test_triangle_area_valid_value_irregular_triangle_large(self):
        self.assertAlmostEqual(area(12345678, 13457680, 15232348), 79101678940186.55, 2)

    def test_triangle_area_valid_value_irregular_triangle_float(self):
        self.assertAlmostEqual(area(1.2, 5.3, 6.1), 2.5350, 4)


class GeometryTestTriangleInvalidArea(unittest.TestCase):
    def test_triangle_area_invalid_value_degenerate_triangle(self):
        self.assertRaises(ValueError, area, 12, 2, 3)

    def test_triangle_area_invalid_value_negative(self):
        self.assertRaises(ValueError, area, -3, 2, -2)

    def test_triangle_area_invalid_value_zeros(self):
        self.assertRaises(ValueError, area, 0, 0, 3)
        self.assertRaises(ValueError, area, 4, 0, 3)
        self.assertRaises(ValueError, area, 4, 2, 0)

    def test_triangle_area_invalid_type_list(self):
        self.assertRaises(TypeError, area, [12], 8, 7)

    def test_triangle_area_invalid_type_list2(self):
        self.assertRaises(TypeError, area, [12], [12], [12])

    def test_triangle_area_invalid_type_bool(self):
        self.assertRaises(TypeError, area, True, False, 49)

    def test_triangle_area_invalid_type_none(self):
        self.assertRaises(TypeError, area, 4, None, None)

    def test_triangle_area_invalid_type_tuple(self):
        self.assertRaises(TypeError, area, (9, 2), (2.4), (3, 4))

    def test_triangle_area_invalid_type_missing_arguments(self):
        self.assertRaises(TypeError, area)

    def test_triangle_area_invalid_type_string(self):
        self.assertRaises(TypeError, area, '32', '43', '23')

    def test_triangle_area_invalid_type_dict(self):
        self.assertRaises(TypeError, area, {'1': 1}, {'1': 3}, {'4': 1})

    def test_triangle_area_invalid_type_two_args(self):
        self.assertRaises(TypeError, area, 2, 5)


class GeometryTestTriangleValidPerimeter(unittest.TestCase):
    def test_triangle_perimeter_valid_value_right_triangle(self):
        self.assertEqual(perimeter(13, 12, 5), 30)

    def test_triangle_perimeter_valid_value_irregular_triangle_large(self):
        self.assertEqual(perimeter(12345678, 13457680, 15232348), 41035706)

    def test_triangle_perimeter_valid_value_irregular_triangle_float(self):
        self.assertEqual(perimeter(1.2, 5.3, 6.1), 12.6)

    def test_triangle_perimeter_valid_value_irregular_triangle(self):
        self.assertEqual(perimeter(12, 8, 9), 29)


class GeometryTestTriangleInvalidPerimeter(unittest.TestCase):
    def test_triangle_perimeter_invalid_value_degenerate_triangle(self):
        self.assertRaises(ValueError, perimeter, 12, 2, 3)

    def test_triangle_perimeter_invalid_value_negative(self):
        self.assertRaises(ValueError, perimeter, -3, 2, -2)

    def test_triangle_perimeter_invalid_value_zeros(self):
        self.assertRaises(ValueError, perimeter, 0, 0, 3)
        self.assertRaises(ValueError, perimeter, 4, 0, 3)
        self.assertRaises(ValueError, perimeter, 4, 2, 0)

    def test_triangle_perimeter_invalid_type_list(self):
        self.assertRaises(TypeError, perimeter, [12], 8, 7)

    def test_triangle_perimeter_invalid_type_list2(self):
        self.assertRaises(TypeError, perimeter, [12], [12], [12])

    def test_triangle_perimeter_invalid_type_bool(self):
        self.assertRaises(TypeError, perimeter, True, False, 49)

    def test_triangle_perimeter_invalid_type_none(self):
        self.assertRaises(TypeError, perimeter, 4, None, None)

    def test_triangle_perimeter_invalid_type_tuple(self):
        self.assertRaises(TypeError, area, (9, 2), (2.4), (3, 4))

    def test_triangle_perimeter_invalid_type_missing_arguments(self):
        self.assertRaises(TypeError, perimeter)

    def test_triangle_perimeter_invalid_type_string(self):
        self.assertRaises(TypeError, perimeter, '32', '43', '23')

    def test_triangle_perimeter_invalid_type_dict(self):
        self.assertRaises(TypeError, perimeter, {'1': 1}, {'1': 3}, {'4': 1})

    def test_triangle_perimeter_invalid_type_two_args(self):
        self.assertRaises(TypeError, perimeter, 2, 5)
