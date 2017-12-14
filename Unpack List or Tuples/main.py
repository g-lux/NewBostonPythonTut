# long way
# item = ['December 23, 2015', 'Bread Gloves', 8.51]
# date = item[0]

# variable and list have to match
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
print(name)


def drop_first_last(grades):
    # grade is a list. Store the first, then everything in the middle, finally last. Allows dynamic list size
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([1, 2, 3, 4, 5, 6, 7, 8])
