#!/usr/bin/python3
"""
Unittest for Base
"""
import unittest
Base = __import__('models.base').Base

class TestBase(unittest.TestCase):
    def test_none(self):
        """
            return None when list is empty
        """
        self.assertAlmostEqual(Base(), None)
