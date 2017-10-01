#! /usr/bin/env python3
"""Sample code to read in test cases:"""

import unittest 
import easy18_solution as sut


class Testeasy18(unittest.TestCase):
    def test_parse(self):
        self.assertEqual((0, 0), sut.parse("0,0"))
        self.assertEqual((1, 1), sut.parse("1,1"))
        self.assertEqual((10, 10), sut.parse("10,10"))

    def test_find_smallest_multippel_greater_than(self):
        self.assertEqual(1, sut.find_smallest_multippel_greater_than(1, 1))
        self.assertEqual(10, sut.find_smallest_multippel_greater_than(9, 5))


if __name__ == '__main__':
    unittest.main()
