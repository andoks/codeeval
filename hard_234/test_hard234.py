#! /usr/bin/env python3

import unittest
import hard234 as sut


class TestHard234(unittest.TestCase):
    def test_get_chars(self):
        self.assertEqual([], sut.get_chars(""))
        self.assertEqual(['a'], sut.get_chars("a"))
        self.assertEqual(['a', 'b', 'c'], sut.get_chars("abc"))
        self.assertEqual(['a', ' ', 'b', ' ', 'c'], sut.get_chars("a b c"))
        self.assertEqual(["i", "l", "o", "v", "e", "c", "o", "d", "e", "e", "v", "a", "l"], sut.get_chars("ilovecodeeval"))

    def test_count_chars(self):
        self.assertEqual({}, sut.count_chars([]))
        self.assertEqual({"a": 1}, sut.count_chars(["a"]))
        self.assertEqual({"a": 1, "b": 1}, sut.count_chars(["a", "b"]))
        self.assertEqual({"a": 2}, sut.count_chars(["a", "a"]))
        self.assertEqual({"a": 2, "b": 2}, sut.count_chars(["a", "b", "a", "b"]))
        self.assertEqual({"a": 2, "b": 2, " ": 3}, sut.count_chars(["a"," ", "b", " ", "a", " ", "b"]))
        self.assertEqual({"i": 1, "l": 2, "o": 2, "v": 2, "e": 3, "c": 1, "d": 1, "a": 1}
, sut.count_chars(["i", "l", "o", "v", "e", "c", "o", "d", "e", "e", "v", "a", "l"]))

    def test_is_left_right_ok_leafs(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        self.assertTrue(sut.is_left_right_ok(a, b))
        self.assertFalse(sut.is_left_right_ok(b, a))

    def test_is_left_right_ok_tree(self):
        a = ("a", (2, None, None))
        b = ("b", (1, None, None))
        c = ("c", (1, None, None))
        bc = ("bc", (2, b, c))
        self.assertTrue(sut.is_left_right_ok(bc, a))
        self.assertFalse(sut.is_left_right_ok(a, bc))

    def test_is_left_right_ok_many_chars(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        c = ("c", (2, None, None))
        ab = ("ab", (2, a, b))
        self.assertTrue(sut.is_left_right_ok(ab, c))
        self.assertFalse(sut.is_left_right_ok(c, ab))

    def test_make_tree_from_dict(self):
        d1 = [] 
        self.assertEqual(d1, sut.make_tree_from_dict({}))
        d2 = [("a", (1, None, None))]
        self.assertEqual(d2, sut.make_tree_from_dict({"a": 1}))
        d3 = [("a", (1, None, None)), ("b", (2, None, None))]
        self.assertEqual(d3, sut.make_tree_from_dict({"a": 1, "b": 2}))

    def test_make_tree_from_dict_ilove(self):
        loveNodes = []
        loveNodes.append(("i", (1, None, None)))
        loveNodes.append(("d", (1, None, None)))
        loveNodes.append(("c", (1, None, None)))
        loveNodes.append(("a", (1, None, None)))
        loveNodes.append(("v", (2, None, None)))
        loveNodes.append(("o", (2, None, None)))
        loveNodes.append(("l", (2, None, None)))
        loveNodes.append(("e", (3, None, None)))
        loveDict = {"i": 1, "l": 2, "o": 2, "v": 2, "e": 3, "c": 1, "d": 1, "a": 1}
        generated = sorted(sut.make_tree_from_dict(loveDict))
        reference = sorted(loveNodes)
        self.assertEqual(reference, generated)


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

    def test_build_huffman_tree_ilove(self):
        loveDict = {"i": 1, "l": 2, "o": 2, "v": 2, "e": 3, "c": 1, "d": 1, "a": 1}
        a = ("a", (1, None, None))
        c = ("c", (1, None, None))
        d = ("d", (1, None, None))
        i = ("i", (1, None, None))
        l = ("l", (2, None, None))
        o = ("o", (2, None, None))
        v = ("v", (2, None, None))
        e = ("e", (3, None, None))

        di = ("di", (2, d, i))
        ac = ("ac", (2, a, c))
        acdi = ("acdi", (4, ac, di))
        lo = ("lo", (4, l, o))
        ve = ("ve", (5, v, 4))
        acdilo = ("acdilo", (8, acdi, lo))
        veacdilo = ("veacdilo", (13, ve, acdilo))
        loveTree = veacdilo

        self.assertEqual(loveTree, sut.build_huffman_tree(loveDict))

    def test_get_codes_for_nodes_leaf_nodes_alphabetical_when_equal_weight(self):
        a = ("a", (1, None, None))
        b = ("b", (1, None, None))
        c = ("c", (2, None, None))
        ab = ("ab", (2, a, b))
        abc = ("cab", (4, ab, c))
        self.assertEqual({"a": "00", "b": "01", "c": "1"}, sut.get_codes_for_nodes(abc))

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
