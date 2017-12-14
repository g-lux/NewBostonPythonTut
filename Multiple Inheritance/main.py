# Use multiple inheritance to pass multiple small classes into one big class

class Mario():
    def move(self):
        print('I am moving')


class Shroom():
    def eat_shroom(self):
        print('Now I am big')


class Big_Mario(Mario, Shroom):
    # Use pass if you don't need to def functions in master class
    pass


bm = Big_Mario()
bm.move()
bm.eat_shroom()
