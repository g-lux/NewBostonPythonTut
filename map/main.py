income = [10, 30, 75]


def double_money(dollars):
    return dollars * 2


map(double_money, income)

# map method
new_income = list(map(double_money, income))
print(new_income)

# for loop method
new_list = []
for item in income:
    new_list.append(item * 2)
print(new_list)
