#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class to test max_integer"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, -3, 2]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_float(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.5, 4.5, 3.5, 2.5]), 4.5)
        self.assertEqual(max_integer([4.5, -2.5, 3.5, 1.5]), 4.5)

    def test_max_negativ(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]),None)

    def test_max_negative_float(self):
        self.assertEqual(max_integer([-1.5, -2.89, -3.43, -4.5]), -1.5)

    def test_string(self):
        self.assertEqual(max_integer("Hello"), 'o')

    def test_list_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer([[1.5, 2.3], [3.3, 4.8]]), [3.3, 4.8])

    def tset_tuple(self):
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((7, 9, 3, 5)), 9)

    def test_list_tupls(self):
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))
        self.assertEqual(max_integer([(1.5, 2.3), (3.3, 4.8)]), (3.3, 4.8))
