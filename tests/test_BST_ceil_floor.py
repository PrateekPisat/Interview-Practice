from BST_ceil_floor import find_BST_ceil_floor, Node


def build_test_bst():
    r"""
    Construct below tree:
                   8
                 /   \
                /     \
               4       10
              / \     /  \
             /   \   /    \
            2     6 9     12
    """
    root = Node(8)
    n1 = Node(4)
    n2 = Node(10)
    n3 = Node(2)
    n4 = Node(6)
    n5 = Node(9)
    n6 = Node(12)

    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    return root


bst_to_test = build_test_bst()


def test_find_BST_ceil_floor_1():
    c, f = find_BST_ceil_floor(bst_to_test, 1)
    assert f is None
    assert c == 2


def test_find_BST_ceil_floor_2():
    c, f = find_BST_ceil_floor(bst_to_test, 3)
    assert f == 2
    assert c == 4


def test_find_BST_ceil_floor_3():
    c, f = find_BST_ceil_floor(bst_to_test, 9)
    assert f == 9
    assert c == 9


def test_find_BST_ceil_floor_4():
    c, f = find_BST_ceil_floor(bst_to_test, 7)
    assert f == 6
    assert c == 8
