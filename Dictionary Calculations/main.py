stocks = {
    'GOOG': 520.54,
    'FB': 76.34,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

# min will run againt the key. In this case apple is the min (alphabetical order)
print(min(stocks))

# need to create a list or sets of tuples
# (99.76, AAPL) (306.21, AMZN)

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
