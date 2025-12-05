import unittest
from square import *

class GeometryTestSquareValidArea(unittest.TestCase):
    def test_square_area_valid_value(self):
        self.assertEqual(area(12), 144)

    def test_square_area_valid_value_float(self):
        self.assertAlmostEqual(area(3.333), 11.1089, 4)

    def test_square_area_valid_value_large(self):
        self.assertEqual(area(123456780), 15241576527968400)


class GeometryTestSquareInvalidArea(unittest.TestCase):
    def test_rectangle_area_invalid_value_zero(self):
        self.assertRaises(ValueError, area, 0)

    def test_rectangle_area_invalid_value_negative(self):
        self.assertRaises(ValueError, area, -3)

    def test_rectangle_area_invalid_type_list(self):
        self.assertRaises(TypeError, area, [12])

    def test_rectangle_area_invalid_type_empty(self):
        self.assertRaises(TypeError, area)

    def test_rectangle_area_invalid_type_bool(self):
        self.assertRaises(TypeError, area, False)

    def test_rectangle_area_invalid_type_none(self):
        self.assertRaises(TypeError, area, None)

    def test_rectangle_area_invalid_type_set(self):
        self.assertRaises(TypeError, area, {4})

    def test_rectangle_area_invalid_type_string(self):
        self.assertRaises(TypeError, area, '32')

    def test_rectangle_area_invalid_type_tuple(self):
        self.assertRaises(TypeError, area, (2.3, 1))

    def test_rectangle_area_invalid_type_dict(self):
        self.assertRaises(TypeError, area, {'1': 1})

    def test_rectangle_area_invalid_type_two_arguments(self):
        self.assertRaises(TypeError, area, 2, 5)


class GeometryTestSquareValidPerimeter(unittest.TestCase):
    def test_square_perimeter_valid_value(self):
        self.assertEqual(perimeter(12), 48)

    def test_square_perimeter_valid_value_float(self):
        self.assertAlmostEqual(perimeter(3.333), 13.332, 3)

    def test_square_perimeter_valid_value_large(self):
        self.assertEqual(perimeter(123456780), 493827120)


class GeometryTestSquareInvalidPerimeter(unittest.TestCase):
    def test_rectangle_perimeter_invalid_value_zero(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_rectangle_perimeter_invalid_value_negative(self):
        self.assertRaises(ValueError, perimeter, -3)

    def test_rectangle_perimeter_invalid_type_list(self):
        self.assertRaises(TypeError, perimeter, [12])

    def test_rectangle_perimeter_invalid_type_empty(self):
        self.assertRaises(TypeError, perimeter)

    def test_rectangle_perimeter_invalid_type_bool(self):
        self.assertRaises(TypeError, perimeter, False)

    def test_rectangle_perimeter_invalid_type_none(self):
        self.assertRaises(TypeError, perimeter, None)

    def test_rectangle_perimeter_invalid_type_set(self):
        self.assertRaises(TypeError, perimeter, {4})

    def test_rectangle_perimeter_invalid_type_string(self):
        self.assertRaises(TypeError, perimeter, '32')

    def test_rectangle_perimeter_invalid_type_tuple(self):
        self.assertRaises(TypeError, perimeter, (2.3, 1))

    def test_rectangle_perimeter_invalid_type_dict(self):
        self.assertRaises(TypeError, perimeter, {'1': 1})

    def test_rectangle_perimeter_invalid_type_two_arguments(self):
        self.assertRaises(TypeError, perimeter, 2, 5)
