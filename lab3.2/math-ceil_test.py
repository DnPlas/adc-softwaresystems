#! /usr/bin/env python

"""
This program tests the math.ceil() method
"""

import math
import unittest

class TestMathCeil(unittest.TestCase):

    # (R) Right results
    def test_one_dec(self):
        self.assertEqual(math.ceil(8.1),9)
        self.assertEqual(math.ceil(10.5),11)
        self.assertEqual(math.ceil(1540.3),1541)

    def test_five_dec(self):
        self.assertEqual(math.ceil(10.90909),11)
        self.assertEqual(math.ceil(1500.23456),1501)

    def test_zero_dec(self):
        self.assertEqual(math.ceil(10.0),10)
        self.assertEqual(math.ceil(800.0),800)

    def test_integers(self):
        self.assertEqual(math.ceil(10),10)

    def test_large_integers(self):
        self.assertEqual(math.ceil(10.88881234567890987654321223325345293984982),11)
        self.assertEqual(math.ceil(10410984174623469.88881234567890987654321223325345293984982),10410984174623470)

    def test_negatives(self):
        self.assertEqual(math.ceil(-10.1),-10)

    # (C) Cross check
    def test_cross_check(self):
        self.assertEqual(math.ceil(-500.25), -1*math.ceil(499.25))

    # (E) Error conditions
    def test_errors(self):
        self.assertNotEqual(math.ceil(500.1), 500)
        self.assertNotEqual(math.ceil(-10.25), -11)

if __name__=='__main__':
    unittest.main()
