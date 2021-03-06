# Class - template that groups similar functions and variables together

class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + ' life left')


# Object used to access functions and variables inside class. Each object is a copy and independent from each other

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()

enemy2.attack()
enemy2.checkLife()
