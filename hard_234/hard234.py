#! /usr/bin/env python3

from typing import List, Dict, Tuple
import functools


class Node(object):
    def _make_ancestor(self, leftChild: 'Node', rightChild: 'Node') -> 'Node':
        self._value = leftChild.value() + rightChild.value()
        self._priority = leftChild.priority() + rightChild.priority()
        self._leftChild = leftChild
        self._rightChild = rightChild

    def _make_leaf(self, value: str, priority: int) -> 'Node':
        self._value = value
        self._priority = priority
        self._leftChild = None
        self._rightChild = None

    def __init__(self, *args) -> 'Node':
        if len(args) == 2 and isinstance(args[0], Node) and isinstance(args[1], Node):
            self._make_ancestor(args[0], args[1])
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
            self._make_leaf(args[0], args[1])
        else:
            raise ValueError("arguments to ctor is wrong")

    def __eq__(self, other: 'Node') -> bool:
        if self is not None and other is not None:
            return self.value() == other.value() and self.priority() == other.priority() and self._leftChild == other._leftChild and self._rightChild == other._rightChild
        else:
            return False

    def __repr__(self) -> str:
        return "[{}: {} - l: {} r: {}]".format(self.value(), self.priority(),self._leftChild, self._rightChild)

    def left_most_leaf(self) -> 'Node':
        if self._leftChild is None:
            return self
        else:
            return self._leftChild

    def priority(self) -> int:
        return self._priority

    def value(self) -> str:
        return self._value

    def get_codes_for_nodes(self, code_so_far: str = "") -> Dict[str, str]:
        codes = {}
        left = self._leftChild
        right = self._rightChild
        if left == None and right == None:
            return {self.value(): code_so_far}
        else:
            if left != None:
                codes.update(left.get_codes_for_nodes(code_so_far + "0"))
            if right != None:
                codes.update(right.get_codes_for_nodes(code_so_far + "1"))
    
            return codes

def is_left_ok(lhs: Node, rhs: Node) -> bool:
    if lhs.priority() != rhs.priority():
        return lhs.priority() - rhs.priority()
    else:
        left_leaf = lhs.left_most_leaf()
        rhs_leaf = rhs.left_most_leaf()
        if left_leaf.priority() != rhs_leaf.priority():
            return left_leaf.priority() - rhs_leaf.priority()
        else:
            if left_leaf.value() < rhs_leaf.value():
                return -1
            elif left_leaf.value() > rhs_leaf.value():
                return 1
            else:
                return 0

def get_chars(line: str) -> List[str]:
    return [x for x in line]

def count_chars(char_list: List[str]) -> Dict[str, int]:
    charToCount = {}
    for char in char_list:
        if char in charToCount:
            charToCount[char] += 1
        else:
            charToCount[char] = 1

    return charToCount

def build_huffman_tree(charsToCount: Dict[str, int]):
    tree = make_trees_from_dict(charsToCount)
    while len(tree) > 1:
        tree = sorted(tree, key=functools.cmp_to_key(is_left_ok))
        left = tree[0]
        right = tree[1]
        tree.remove(left)
        tree.remove(right)
        combined = Node(left, right)
        tree.append(combined)

    return tree[0] if len(tree) == 1 else None

def make_trees_from_dict(charsToCount: Dict[str, int]) -> List[Node]:
    tree = [Node(key, charsToCount[key]) for key in charsToCount]
    return tree

def make_ordered_output_string(charsToCode: Dict[str, str]) -> str:
    in_order = [n for n in sorted(charsToCode.items(), key=lambda entry: entry[0])]
    entries_as_strings = []
    for entry in in_order:
        entries_as_strings.append(entry[0] + ": " + entry[1] + ";")

    return " ".join(entries_as_strings)

def get_huffman_weights(line: str) -> str:
    characters = get_chars(line)
    charsToCount = count_chars(characters)
    huffmanTree = build_huffman_tree(charsToCount)
    charsToCode = huffmanTree.get_codes_for_nodes()
    output = make_ordered_output_string(charsToCode)
    
    return output

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print(get_huffman_weights(line))

