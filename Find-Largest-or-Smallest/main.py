import heapq

grades = [32, 43, 57, 89, 95, 92, 64, 22, 45]

print(heapq.nlargest(3, grades))

stocks = [
    {'t': 'GOOG', 'p': 520.54},
    {'t': 'FB', 'p': 212},
    {'t': 'MG', 'p': 52312},
    {'t': 'AC', 'p': 2234},
    {'t': 'PP', 'p': 521235}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['p']))
