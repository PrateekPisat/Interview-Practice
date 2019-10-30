"""
Problem:
    Given a binary search tree, find the floor and ceiling of a given integer.
    The floor is the highest element in the tree less than or equal to an
    integer,while the ceiling is the lowest element in the tree greater
    than or equal to an integer. If either value does not exist, return None.
"""


class Node:
    """Represents a Node in a BST."""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_ceil_floor(ip, root, floor, ceil):
    """Return the floor and ceil for given input in given BST.

    :param ip: The input integer.
    :param root: The root node for the BST.
    :param floor: The current floor.
    :param ceil: The current ceil.
    """
    if root:
        if root.data == ip:
            floor = ceil = ip
            return (ceil, floor)
        elif root.data > ip:
            ceil = root.data
            return find_ceil_floor(ip, root.left, floor, ceil)
        else:
            floor = root.data
            return find_ceil_floor(ip, root.right, floor, ceil)
    else:
        return (ceil, floor)


def find_BST_ceil_floor(root, ip):
    return find_ceil_floor(ip, root, None, None)
