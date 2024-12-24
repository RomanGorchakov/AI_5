#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"

def ids(root, goal):
    depth = 0
    while True:
        found, path = dls(root, goal, depth)
        if found:
            return path
        depth += 1

def dls(node, goal, depth):
    if depth == 0:
        if node.value == goal:
            return True, [node.value]
        else:
            return False, []

    if depth > 0:
        for child in node.children:
            found, path = dls(child, goal, depth - 1)
            if found:
                return True, [node.value] + path

    return False, []


if __name__ == '__main__':
    root = TreeNode("dir")
    root.add_child(TreeNode("dir2"))
    root.add_child(TreeNode("dir3"))
    root.children[0].add_child(TreeNode("file4"))
    root.children[1].add_child(TreeNode("file5"))
    root.children[1].add_child(TreeNode("file6"))

    goal = "file5"

    path = ids(root, goal)
    if path:
        print(" -> ".join(path))
    else:
        print("Файл не найден")