# import pytest
#
# from stock_prices import get_max_profit
#
#
# @pytest.mark.parametrize(
#     "stock_prices, expected",
#     [
#         ([7,1,5,3,6,4], 5),
#         ([10, 7, 5, 8, 11, 9], 6),
#         ([7,6,4,3,1], 0),
#         ([1, 0], 0),
#         ([1], 0),
#         ([], 0),
#     ]
# )
# def test_get_max_profit(stock_prices, expected):
#     res = get_max_profit(stock_prices)
#     assert res == expected
