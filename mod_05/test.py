#! /usr/bin/env python

import main
import unittest

class TestMod05(unittest.TestCase):
    def test_make_number_list_empty_string(self):
        self.assertEqual([], main.make_number_list(""))

    def test_make_number_list_single_number(self):
        self.assertEqual([1], main.make_number_list("1"))

    def test_make_number_list_many_numbers(self):
        self.assertEqual([1, 2, 33], main.make_number_list("1 2 33"))

    def test_find_cycle_empty(self):
        self.assertEqual([], main.find_cycle([]))

    def test_find_cycle_no_cycle(self):
        self.assertEqual([], main.find_cycle([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]))

    def test_find_cycle_one_number_repeating_once(self):
        self.assertEqual([1], main.find_cycle([1, 1]))

    def test_find_cycle_one_cycle(self):
        self.assertEqual([1, 2], main.find_cycle([1, 2, 1, 2]))

    def test_find_cycle_first_cycle_with_many(self):
        self.assertEqual([1, 2], main.find_cycle([1, 2, 1, 2, 3, 4, 3, 4]))

    def test_find_cycle_first_cycle_with_many_numbers_in_it(self):
        self.assertEqual([1, 2, 3], main.find_cycle([1, 2, 3, 1, 2, 3]))

    def test_find_cycle_first_cycle_with_many_consecutive_cycles(self):
        self.assertEqual([49], main.find_cycle([49, 49, 49, 49]))

    def test_make_string_empty(self):
        self.assertEqual("", main.make_string([]))

    def test_make_string_with_nums(self):
        self.assertEqual("1 2 3", main.make_string([1, 2, 3]))

    def test_make_string_with_nums_unsorted(self):
        self.assertEqual("11 33 22", main.make_string([11, 33, 22]))

