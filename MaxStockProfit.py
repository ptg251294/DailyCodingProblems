# Given a array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell
# it at 10 dollars.
# [40, 2, 1, 20, 1, 10] = 19


def calculate_max_profit(price_list):
    buying_price = price_list[0]
    possible_profits = [0]
    for index in range(1, len(price_list)):
        current_price = price_list[index]
        if current_price < buying_price:
            buying_price = current_price
        else:
            possible_profits.append(current_price - buying_price)
    profit = max(possible_profits)
    if profit == 0:
        print('Profit not possible.')
    else:
        print(profit)


if __name__ == '__main__':
    stock_prices = [40, 2, 1, 20, 1, 10]
    calculate_max_profit(stock_prices)
