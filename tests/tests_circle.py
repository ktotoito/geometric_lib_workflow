import unittest
from circle import *


class GeometryTestCircleValidArea(unittest.TestCase):
    def test_circle_valid_value(self):
        self.assertAlmostEqual(area(12), 452.3893, 4)

    def test_circle_valid_value_float(self):
        self.assertAlmostEqual(area(5.5), 95.0332, 4)

    def test_circle_valid_value_large(self):
        self.assertAlmostEqual(area(12345678), 478828248493921.5, 1)


class GeometryTestCircleInvalidArea(unittest.TestCase):
    def test_circle_area_invalid_value_zero(self):
        self.assertRaises(ValueError, area, 0)

    def test_circle_area_invalid_value_negative(self):
        self.assertRaises(ValueError, area, -3)

    def test_circle_area_invalid_type_empty(self):
        self.assertRaises(TypeError, area)

    def test_circle_area_invalid_type_bool(self):
        self.assertRaises(TypeError, area, False)

    def test_circle_area_invalid_type_list(self):
        self.assertRaises(TypeError, area, [12])

    def test_circle_area_invalid_type_set(self):
        self.assertRaises(TypeError, area, {4})

    def test_circle_area_invalid_type_string(self):
        self.assertRaises(TypeError, area, '32')

    def test_circle_area_invalid_type_none(self):
        self.assertRaises(TypeError, area, None)

    def test_circle_area_invalid_type_tuple(self):
        self.assertRaises(TypeError, area, (2.3, 1))

    def test_circle_area_invalid_type_dict(self):
        self.assertRaises(TypeError, area, {'1':1})


class GeometryTestCircleValidPerimeter(unittest.TestCase):
    def test_perimeter_valid_value(self):
        self.assertAlmostEqual(perimeter(12), 75.3982, 4)

    def test_perimeter_valid_value_float(self):
        self.assertAlmostEqual(perimeter(6.22), 39.0814, 4)

    def test_perimeter_valid_value_large(self):
        self.assertAlmostEqual(perimeter(12345678), 77570182.6168, 4)


class GeometryTestCircleInvalidPerimeter(unittest.TestCase):
    def test_circle_perimeter_invalid_value_zero(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_circle_perimeter_invalid_value_negative(self):
        self.assertRaises(ValueError, perimeter, -3)

    def test_circle_perimeter_invalid_type_empty(self):
        self.assertRaises(TypeError, perimeter)

    def test_circle_perimeter_invalid_type_bool(self):
        self.assertRaises(TypeError, perimeter, False)

    def test_circle_perimeter_invalid_type_list(self):
        self.assertRaises(TypeError, perimeter, [12])

    def test_circle_perimeter_invalid_type_set(self):
        self.assertRaises(TypeError, perimeter, {4})

    def test_circle_perimeter_invalid_type_string(self):
        self.assertRaises(TypeError, perimeter, '32')

    def test_circle_perimeter_invalid_type_none(self):
        self.assertRaises(TypeError, perimeter, None)

    def test_circle_perimeter_invalid_type_tuple(self):
        self.assertRaises(TypeError, perimeter, (2.3, 1))

    def test_circle_perimeter_invalid_type_dict(self):
        self.assertRaises(TypeError, perimeter, {'1':1})
