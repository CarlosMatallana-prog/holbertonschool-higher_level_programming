#!/usr/bin/python3
"""  test for max_integer  """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test cases"""

    def test_integer_numbers(self):
        """  test max integer in a list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-20]), -20)

    def test_float_numbers(self):
        """  test for float numbers"""
        self.assertEqual(max_integer([1, 2, 4, 10e+1000]), 10e+1000)
        self.assertEqual(max_integer([1.0, 2.4, 4.3, 100.4]), 100.4)
        self.assertEqual(max_integer([-1.0, -2.2, -4.3, -100.4]), -1.0)
        self.assertEqual(max_integer([1, 3, 200, 10000, 100e+1000]), 100e+1000)
        self.assertEqual(max_integer([1, 3, 200, 5000, -100e+1000]), 5000)

    def test_strings(self):
        """  test for strings as arguments"""
        self.assertEqual(max_integer(['pep']), 'pepe')
        self.assertEqual(max_integer('pepe'), 'n')
        self.assertEqual(max_integer(['pepe', 'cortes', 'sully']), 'sully')
        self.assertEqual(max_integer(['H', 'h']), 'h')

    def test_extreme_cases(self):
        """  test for max integer in list of integers"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer((1, 2, 100, -4)), 100)
        self.assertEqual(max_integer([-100e+1000, 100e+1000]), 100e+1000)
        self.assertEqual(max_integer([25 // 5, 1]), 5)

    def test_raise_type(self):
        """  test for raises diferents TypeError"""
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, ['pepe', 2, 5, 20])
        self.assertRaises(TypeError, max_integer, [2, 5, "pepe", 20])
        with self.assertRaises(TypeError):
            max_integer(1, 4, 6, 5)
        with self.assertRaises(TypeError):
            max_integer([1, 2j])
        with self.assertRaises(ValueError):
            max_integer([1, 2, int("four")])
        with self.assertRaises(TypeError):
            max_integer(2)
