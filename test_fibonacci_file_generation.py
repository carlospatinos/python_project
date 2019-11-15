#!/usr/bin/python
import unittest
import sys

from function import mymath as target

class TestSum(unittest.TestCase):
    def test_fib_9(self):
        """
        Test that fibo function returns 34 when input is 9
        """
        data = 9
        result = target.fibFunction(data)
        self.assertEqual(result, 34)

    def test_fib_11(self):
        """
        Test that fibo function returns 89 when input is 11
        """
        data = 11
        result = target.fibFunction(data)
        self.assertEqual(result, 89)

if __name__ == '__main__':
    unittest.main()