from k_sorted_array import sort


def test_sort_best_case():
    arr = [1, 2, 3, 4, 5]
    k = 1
    sorted_array = sort(arr, k)

    assert sorted_array == arr


def test_sort_worst_case():
    arr = [5, 4, 3, 2, 1]
    k = 4
    sorted_array = sort(arr, k)

    assert sorted_array == [1, 2, 3, 4, 5]


def test_sort_avg_case():
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    sorted_array = sort(arr, k)

    assert sorted_array == [2, 3, 5, 6, 8, 9, 10]
