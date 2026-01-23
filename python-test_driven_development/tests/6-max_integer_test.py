#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max integer is at the beginning"""
        self.assertEqual(max_integer([10, 3, 4, 2]), 10)

    def test_max_at_end(self):
        """Test when the max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 50]), 50)

    def test_one_element_list(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list should return None"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        """Test list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

if __name__ == '__main__':
    unittest.main()
