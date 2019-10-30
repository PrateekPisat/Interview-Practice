from quick_sort import quick_sort


def test_quick_sort():
    A = quick_sort([7, 2, 1, 6, 8, 5, 3, 4])
    assert A == [1, 2, 3, 4, 5, 6, 7, 8]
