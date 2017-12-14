class Girl:
    # class variable - shared for between all Girl objects
    gender = 'female'

    def __init__(self, name):
        # instance variable - unique for each Girl object (instance of each class)
        self.name = name


r = Girl('Rachel')
s = Girl('Stanky')

print(r.gender)
print(s.gender)

print(r.name)
print(s.name)
