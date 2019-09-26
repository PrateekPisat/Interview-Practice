def get_max_profit(stock_prices):
    buy = 0
    sell = len(stock_prices) - 1
    max_buy = 9999999999
    max_sell = -1
    buy_index = 0
    sell_index = 1

    if len(stock_prices) == 1 or len(stock_prices) == 0:
        return 0

    while buy <= sell:
        if stock_prices[buy] < max_buy and buy <= sell_index:
            max_buy = stock_prices[buy]
            buy_index = buy
        if stock_prices[sell] > max_sell and sell >= buy_index:
            max_sell = stock_prices[sell]
            sell_index = sell
        buy += 1
        sell -= 1

    return (max_sell - max_buy) if (max_sell - max_buy) >= 0 else 0
