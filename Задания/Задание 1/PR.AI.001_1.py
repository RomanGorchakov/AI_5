#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"

def ids(root, target):
    def depth_limited_search(node, target, depth):
        if node is None:
            return False
        if node.value == target:
            return True
        if depth <= 0:
            return False
        return (depth_limited_search(node.left, target, depth - 1) or
                depth_limited_search(node.right, target, depth - 1))

    depth = 0
    while True:
        found = depth_limited_search(root, target, depth)
        if found:
            return True
        depth += 1


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    left_child = BinaryTreeNode(2)
    right_child = BinaryTreeNode(3)
    root.add_children(left_child, right_child)
    right_child.add_children(BinaryTreeNode(4), BinaryTreeNode(5))

    goal = 4
    result = ids(root, goal)
    print(result)