class Parent():
    def print_last_name(self):
        print('Gluc')


# Pass class in () to inherit
class Child(Parent):
    def print_first_name(self):
        print('Marcin')

    # You can over ride inheritance by defining the same named function in class
    def print_last_name(self):
        print('Snitzleberg')


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()
