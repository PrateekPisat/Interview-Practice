from 0_1_knapsack import knapsack


def test_knapsack():
    res = knapsack(weights=[1, 3, 4, 5], values=[1, 4, 5, 7], total_weight=7)
    assert res == 9
