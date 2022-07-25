#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
            return correct max value
        """
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([5, 4, 5, 8.5, 8]), 8.5)

    def test_none(self):
        """
            return None when list is empty
        """
        self.assertAlmostEqual(max_integer([]), None)

    def test_one(self):
        """
            one element in list
        """
        self.assertAlmostEqual(max_integer([5]), 5)

    def test_types(self):
        """
            all values are not integers
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "4"])
        self.assertRaises(TypeError, max_integer, ["holberton", 2, 3, 4])

    def test_negative(self):
        """
            test for one negative number in the list
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, -4]), 3)
