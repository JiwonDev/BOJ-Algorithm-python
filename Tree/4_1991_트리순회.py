import math
import sys


class MyLib:
    get_line: iter = lambda: map(str, sys.stdin.readline().rstrip().split())
    get_input: int = lambda: int(input())
    print_list = lambda lst: print('\n'.join(map(str, lst)))
    find_indexes = lambda x, lst: [idx for idx, value in enumerate(lst) if value == x]
    # a, b, c = get_line()
    # array:list = list(get_line())
    # a = get_input()
    # print_list(array)
    # for index in find_indexes(value, array)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        if left == ".":
            self.left = None
        else:
            self.left = left

        if right == ".":
            self.right = None
        else:
            self.right = right

    def __str__(self):
        return str(self.data)


def preorder(node: Node, tree: dict):
    print(node.data, end='')
    if node.left is not None:
        preorder(tree[node.left], tree)
    if node.right is not None:
        preorder(tree[node.right], tree)


def postorder(node: Node, tree: dict):
    if node.left is not None:
        postorder(tree[node.left], tree)
    if node.right is not None:
        postorder(tree[node.right], tree)
    print(node.data, end='')


def inorder(node: Node, tree: dict):
    if node.left is not None:
        inorder(tree[node.left], tree)
    print(node.data, end='')
    if node.right is not None:
        inorder(tree[node.right], tree)


def main():
    n = MyLib.get_input()

    tree = {}
    for _ in range(n):
        node, left, right = MyLib.get_line()
        tree[node] = Node(node, left, right)

    root = tree['A']

    preorder(root, tree)
    print()
    inorder(root, tree)
    print()
    postorder(root, tree)
    print()


if __name__ == "__main__":
    main()
