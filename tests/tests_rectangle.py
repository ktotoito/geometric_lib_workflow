import unittest
from rectangle import *


class GeometryTestRectangleValidArea(unittest.TestCase):
    def test_rectangle_area_valid_value(self):
        self.assertEqual(area(1000, 230), 230000)

    def test_rectangle_area_valid_value_large(self):
        self.assertEqual(area(123456780, 123456891), 15241590231670980)

    def test_rectangle_area_valid_value_float(self):
        self.assertEqual(area(6.2, 3.333), 20.6646)


class GeometryTestRectangleValidPerimeter(unittest.TestCase):
    def test_rectangle_perimeter_valid_value(self):
        self.assertEqual(perimeter(1000, 230), 2460)

    def test_rectangle_perimeter_valid_value_large(self):
        self.assertEqual(perimeter(123456780, 123456891), 493827342)

    def test_rectangle_perimeter_valid_value_float(self):
        self.assertAlmostEqual(perimeter(6.2, 3.333), 19.066, 3)


class GeometryTestRectangleInvalidArea(unittest.TestCase):
    def test_rectangle_area_invalid_value_zero_x_valid(self):
        self.assertRaises(ValueError, area, 0, 1)

    def test_rectangle_area_invalid_value_negative_x_valid(self):
        self.assertRaises(ValueError, area, -3, 2)

    def test_rectangle_area_invalid_type_list_x_int(self):
        self.assertRaises(TypeError, area, [12], 1)

    def test_rectangle_area_invalid_type_empty(self):
        self.assertRaises(TypeError, area)

    def test_rectangle_area_invalid_type_bool_x_bool(self):
        self.assertRaises(TypeError, area, False, True)

    def test_rectangle_area_invalid_type_none_x_valid(self):
        self.assertRaises(TypeError, area, None, 2.2)

    def test_rectangle_area_invalid_type_valid_x_set(self):
        self.assertRaises(TypeError, area, 2, {4})

    def test_rectangle_area_invalid_type_string_x_string(self):
        self.assertRaises(TypeError, area, '32', '2.2')

    def test_rectangle_area_invalid_type_tuple_x_tuple(self):
        self.assertRaises(TypeError, area, (2.3, 1), (3,3))

    def test_rectangle_area_invalid_type_valid_x_missing_argument(self):
        self.assertRaises(TypeError, area, 2.3)

    def test_rectangle_area_invalid_type_dict_x_dict(self):
        self.assertRaises(TypeError, area, {'1':1}, {'1':1})


class GeometryTestRectangleInvalidPerimeter(unittest.TestCase):
    def test_rectangle_perimeter_invalid_value_zero_x_valid(self):
        self.assertRaises(ValueError, perimeter, 0, 1)

    def test_rectangle_perimeter_invalid_value_negative_x_valid(self):
        self.assertRaises(ValueError, perimeter, -3, 2)

    def test_rectangle_perimeter_invalid_type_list_x_valid(self):
        self.assertRaises(TypeError, perimeter, [12], 1)

    def test_rectangle_perimeter_invalid_type_empty(self):
        self.assertRaises(TypeError, perimeter)

    def test_rectangle_perimeter_invalid_type_bool_x_bool(self):
        self.assertRaises(TypeError, perimeter, False, True)

    def test_rectangle_perimeter_invalid_type_none_x_valid(self):
        self.assertRaises(TypeError, perimeter, None, 2.2)

    def test_rectangle_perimeter_invalid_type_valid_x_set(self):
        self.assertRaises(TypeError, perimeter, 2, {4})

    def test_rectangle_perimeter_invalid_type_string_x_string(self):
        self.assertRaises(TypeError, perimeter, '32', '2.2')

    def test_rectangle_perimeter_invalid_type_tuple_x_tuple(self):
        self.assertRaises(TypeError, perimeter, (2.3, 1), (3, 3))

    def test_rectangle_perimeter_invalid_type_valid_x_missing_argument(self):
        self.assertRaises(TypeError, perimeter, 2.3)

    def test_rectangle_perimeter_invalid_type_dict_x_dict(self):
        self.assertRaises(TypeError, perimeter, {'1': 1}, {'1': 1})
