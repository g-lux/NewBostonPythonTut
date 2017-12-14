stocks = {
    'GOOG': 520.54,
    'FB': 76.34,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

# use zip function to take dictionary and construct a list of tuples
print(max(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
