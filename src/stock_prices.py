def get_max_profit(prices):
    max_buy = 0
    max_profix = 0
    for price in prices:
        if price >= max_buy:
            max_buy = price
        if max_buy - price >= max_profix:
            max_profix = max_buy - price

    return max_profix
