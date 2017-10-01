#! /usr/bin/env python3

import unittest
import hard234 as sut


class TestHard234(unittest.TestCase):
    def test_get_chars(self):
        self.assertEqual([], sut.get_chars(""))
        self.assertEqual(['a'], sut.get_chars("a"))
        self.assertEqual(['a', 'b', 'c'], sut.get_chars("abc"))
        self.assertEqual(['a', ' ', 'b', ' ', 'c'], sut.get_chars("a b c"))

    def test_count_chars(self):
        self.assertEqual({}, sut.count_chars([]))
        self.assertEqual({"a": 1}, sut.count_chars(["a"]))
        self.assertEqual({"a": 1, "b": 1}, sut.count_chars(["a", "b"]))
        self.assertEqual({"a": 2}, sut.count_chars(["a", "a"]))
        self.assertEqual({"a": 2, "b": 2}, sut.count_chars(["a", "b", "a", "b"]))
        self.assertEqual({"a": 2, "b": 2, " ": 3}, sut.count_chars(["a"," ", "b", " ", "a", " ", "b"]))

    def test_is_left_right_ok(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        self.assertTrue(sut.is_left_right_ok(a, b))
        self.assertFalse(sut.is_left_right_ok(b, a))

    def test_make_tree_from_dict(self):
        d1 = [] 
        self.assertEqual(d1, sut.make_tree_from_dict({}))
        d2 = [("a", (1, None, None))]
        self.assertEqual(d2, sut.make_tree_from_dict({"a": 1}))
        d3 = [("a", (1, None, None)), ("b", (2, None, None))]
        self.assertEqual(d3, sut.make_tree_from_dict({"a": 1, "b": 2}))

    def test_make_combined_node(self):
        cn1 = ("ab", (2, ("a", (1, None, None)), ("b", (1, None, None))))
        self.assertEqual(cn1, sut.make_combined_node(("a", (1, None, None)), ("b", (1, None, None))))
        left2 = ("a", (2, None, None))
        rightLeft = ("b", (1, None, None))
        rightRight = ("c", (1, None, None))
        right2 = ("bc", (2, rightLeft, rightRight))
        cn2 = ("abc", (4, left2, right2))
        self.assertEqual(cn2, sut.make_combined_node(left2, right2))

    def test_build_huffman_tree_empty(self):
        self.assertEqual(None, sut.build_huffman_tree({}))

    def test_build_huffman_tree_alphabetical_if_equal_weight(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        ab = ("ab", (2, a, b))
        self.assertEqual(ab, sut.build_huffman_tree({"a": 1, "b": 1}))
        self.assertEqual(ab, sut.build_huffman_tree({"b": 1, "a": 1}))

    def test_build_huffman_tree(self):
        a = ("a", (1, None, None))
        b = ("b", (2, None, None))
        ab = ("ab", (3, a, b))
        c = ("c", (4, None, None))
        abc = ("abc", (7, ab, c))
        self.assertEqual(a, sut.build_huffman_tree({"a": 1}))
        self.assertEqual(ab, sut.build_huffman_tree({"a": 1, "b": 2}))
        self.assertEqual(abc, sut.build_huffman_tree({"a": 1, "b": 2, "c": 4}))

    def test_get_codes_for_nodes_leaf_nodes_alphabetical_when_equal_weight(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        ab = ("ab", (2, a, b))
        self.assertEqual({"a": "0", "b": "1"}, sut.get_codes_for_nodes(ab))

    def test_get_codes_for_nodes_leaf_nodes_with_different_weight(self):
        a = ("a", (1, None, None))
        b = ("b", (2, None, None))
        c = ("c", (3, None, None))
        ab = ("ab", (3, a, b))
        abc = ("abc", (6, ab, c))

        self.assertEqual({"a": "00", "b": "01", "c": "1"}, sut.get_codes_for_nodes(abc))

    def test_make_ordered_output_string(self):
        self.assertEqual("a: 00; b: 01; c: 1;", sut.make_ordered_output_string({"a": "00", "b": "01", "c": "1"}))
        self.assertEqual(" : 00; b: 01; c: 1;", sut.make_ordered_output_string({" ": "00", "b": "01", "c": "1"}))

    def test_get_huffman_weights(self):
        #self.assertEqual("", sut.get_huffman_weights(""))
        self.assertEqual("a: 0; b: 1;", sut.get_huffman_weights("ab"))
        self.assertEqual("a: 10; b: 11; c: 0;", sut.get_huffman_weights("abc"))
        self.assertEqual("a: 1000; c: 1001; d: 1010; e: 01; i: 1011; l: 110; o: 111; v: 00;", sut.get_huffman_weights("ilovecodeeval"))

if __name__ == '__main__':
    unittest.main()
