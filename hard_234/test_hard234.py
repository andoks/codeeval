#! /usr/bin/env python3

import hard234 as sut

import unittest
import functools

class TestNode(unittest.TestCase):
    def test_init_leaf(self):
        node = sut.Node("a", 42)
        self.assertEqual("a", node.value())
        self.assertEqual(42, node.priority())
        self.assertIsNone(node._leftChild)
        self.assertIsNone(node._rightChild)

    def test_init_ancestor(self):
        a = sut.Node("a", 42)
        b = sut.Node("b", 1337)
        node = sut.Node(a, b) 
        self.assertEqual("ab", node.value())
        self.assertEqual(42+1337, node.priority())
        self.assertEqual(a, node._leftChild)
        self.assertEqual(b, node._rightChild)

    def test_compare_leafs(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 1)
        self.assertGreater(0, sut.is_left_ok(a, b))
        self.assertLess(0, sut.is_left_ok(b, a))

    def test_compare_tree(self):
        a = sut.Node("a", 2)
        b = sut.Node("b", 1)
        c = sut.Node("c", 1)
        bc = sut.Node(b, c)
        self.assertGreater(0, sut.is_left_ok(bc, a))
        self.assertLess(0, sut.is_left_ok(a, bc))

    def test_compare_many_chars(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 1)
        c = sut.Node("c", 2)
        ab = sut.Node(a, b)
        self.assertGreater(0, sut.is_left_ok(ab, c))
        self.assertLess(0, sut.is_left_ok(c, ab))

    def test_get_codes_for_nodes_leaf_nodes_alphabetical_when_equal_weight(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 1)
        c = sut.Node("c", 2)
        ab = sut.Node(a, b)
        abc = sut.Node(ab, c)
        self.assertEqual({"a": "00", "b": "01", "c": "1"}, abc.get_codes_for_nodes())

    def test_get_codes_for_nodes_leaf_nodes_with_different_weight(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 2)
        c = sut.Node("c", 3)
        ab = sut.Node(a, b)
        abc = sut.Node(ab, c)

        self.assertEqual({"a": "00", "b": "01", "c": "1"}, abc.get_codes_for_nodes())

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


    def test_make_trees_from_dict(self):
        d1 = [] 
        self.assertEqual(d1, sut.make_trees_from_dict({}))
        d2 = [sut.Node("a", 1)]
        self.assertEqual(d2, sut.make_trees_from_dict({"a": 1}))
        d3 = [sut.Node("a", 1), sut.Node("b", 2,)]
        self.assertEqual(d3, sut.make_trees_from_dict({"a": 1, "b": 2}))

    def test_make_trees_from_dict_ilove(self):
        loveNodes = []
        loveNodes.append(sut.Node("i", 1))
        loveNodes.append(sut.Node("d", 1))
        loveNodes.append(sut.Node("c", 1))
        loveNodes.append(sut.Node("a", 1))
        loveNodes.append(sut.Node("v", 2))
        loveNodes.append(sut.Node("o", 2))
        loveNodes.append(sut.Node("l", 2))
        loveNodes.append(sut.Node("e", 3))
        loveDict = {"i": 1, "l": 2, "o": 2, "v": 2, "e": 3, "c": 1, "d": 1, "a": 1}
        generated = sorted(sut.make_trees_from_dict(loveDict), key=functools.cmp_to_key(sut.is_left_ok))
        reference = sorted(loveNodes, key=functools.cmp_to_key(sut.is_left_ok))
        self.assertEqual(reference, generated)

    def test_build_huffman_tree_empty(self):
        self.assertEqual(None, sut.build_huffman_tree({}))

    def test_build_huffman_tree_alphabetical_if_equal_weight(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 1)
        ab = sut.Node(a, b)
        self.assertEqual(ab, sut.build_huffman_tree({"a": 1, "b": 1}))

    def test_build_huffman_tree(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 2)
        ab = sut.Node(a, b)
        c = sut.Node("c", 4)
        abc = sut.Node(ab, c)
        self.assertEqual(ab, sut.build_huffman_tree({"a": 1, "b": 2}))
        self.assertEqual(abc, sut.build_huffman_tree({"a": 1, "b": 2, "c": 4}))

    def test_build_huffman_tree_ilove(self):
        loveDict = {"i": 1, "l": 2, "o": 2, "v": 2, "e": 3, "c": 1, "d": 1, "a": 1}
        a = sut.Node("a", 1)
        c = sut.Node("c", 1)
        d = sut.Node("d", 1)
        i = sut.Node("i", 1)
        l = sut.Node("l", 2)
        o = sut.Node("o", 2)
        v = sut.Node("v", 2)
        e = sut.Node("e", 3)

        di = sut.Node(d, i)
        ac = sut.Node(a, c)
        acdi = sut.Node(ac, di)
        lo = sut.Node(l, o)
        ve = sut.Node(v, e)
        acdilo = sut.Node(acdi, lo)
        veacdilo = sut.Node(ve, acdilo)
        loveTree = veacdilo

        self.assertEqual(loveTree, sut.build_huffman_tree(loveDict))

    def test_sort_nodes_1(self):
        a = sut.Node("a", 1)
        b = sut.Node("b", 1)
        c = sut.Node("c", 1)

        ref = [a, b, c]
        output = sut.sort_nodes([b, a, c])
        self.assertEqual(ref, output)

    def test_sort_nodes_2(self):
        b = sut.Node("b", 1)
        c = sut.Node("c", 2)
        a = sut.Node("a", 4)
        z = sut.Node("z", 1)

        ref = [b, z, c, a]
        output = sut.sort_nodes([b, z, c, a])
        self.assertEqual(ref, output)

    def test_sort_nodes_3(self):
        b = sut.Node("b", 1)
        c = sut.Node("c", 2)
        a = sut.Node("a", 4)
        z = sut.Node("z", 1)

        bc = sut.Node(b, c)
        zbc = sut.Node(z, bc)

        ref = [zbc, a]
        output = sut.sort_nodes([a, zbc])
        self.assertEqual(ref, output)

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
