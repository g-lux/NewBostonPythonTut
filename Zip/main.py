first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)
# [(Bucky, Roberts), (Tom, Hanks)]

# need to loop through it since print(names) returns a list object
for a, b in names:
    print(a, b)
