#! /usr/bin/env python3

from typing import List, Dict, Tuple

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
    tree = make_tree_from_dict(charsToCount)
    while len(tree) > 1:
        tree = sorted(tree, key=lambda node: node[1][0])
        left = tree[0]
        right = tree[1]
        tree.remove(left)
        tree.remove(right)
        left, right = (left, right) if is_left_right_ok(left, right) else (right, left)
        combined = make_combined_node(left, right)
        tree.append(combined)

    return tree[0] if len(tree) == 1 else None

Node = Tuple[str, Tuple[int, 'Node', 'Node']]

def is_left_right_ok(left: Node, right: Node) -> bool:
    if left[1][0] < right[1][0]:
        return True
    elif left[1][0] == right[1][0] and left[0] < right[0]:
        return True
    else:
        return False

def make_tree_from_dict(charsToCount: Dict[str, int]) -> List[Node]:
    tree = [(key, (charsToCount[key], None, None)) for key in charsToCount]
    return tree

def make_combined_node(left, right):
    return (left[0] + right[0], (left[1][0]+right[1][0], left, right))

def get_codes_for_nodes(tree: Node, code_so_far: str = "") -> Dict[str, str]:
    codes = {}
    left = tree[1][1]
    right = tree[1][2]
    if left == None and right == None:
        return {tree[0]: code_so_far}
    else:
        if left != None:
            codes.update(get_codes_for_nodes(left, code_so_far + "0"))
        if right != None:
            codes.update(get_codes_for_nodes(right, code_so_far + "1"))

        return codes

def make_ordered_output_string(charsToCode: Dict[str, str]) -> str:
    in_order = [n for n in sorted(charsToCode.items(), key=lambda entry: entry[0])]
    entries_as_strings = []
    for entry in in_order:
        entries_as_strings.append(entry[0] + ": " + entry[1] + ";")

    return " ".join(entries_as_strings)

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            characters = get_chars(line)
            charsToCount = count_chars(characters)
            huffmanTree = build_huffman_tree(charsToCount)
            charsToCode = get_codes(huffmanTree)
            output = make_ordered_output_string(charsToCode)
            
            print(output)

