#! /usr/bin/env python

"""
This program tests the filecmp.cmp() method
"""

import filecmp
import unittest

file_1 = "text_1.txt"
file_1_clone = "text_1_clone.txt"
file_2 = "text_2.txt"

class TestFilecmpCMP(unittest.TestCase):

    # (R) Right
    def test_comparison(self):
        self.assertTrue(filecmp.cmp(file_1, file_1_clone))

    def test_comparison_false(self):
        self.assertFalse(filecmp.cmp(file_1, file_2))

    def test_contents_eq(self):
        self.assertTrue(filecmp.cmp(file_1, file_1_clone, shallow=False))

    def test_contents_diff(self):
        self.assertFalse(filecmp.cmp(file_1, file_2, shallow=False))

    def test_cache(self):
        self.assertTrue(filecmp.cmp(file_1, file_1_clone, shallow=False))

if __name__=='__main__':
    unittest.main()
