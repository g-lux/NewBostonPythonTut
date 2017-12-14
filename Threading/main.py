# Use threading to run multiple things at once. IE - messaging app will send and receive at the same time

import threading


class MarcinsMessenger(threading.Thread):
    def run(self):
        # Use _ if you don't care about the variable
        for _ in range(1000):
            print(threading.current_thread().getName())


x = MarcinsMessenger(name='Send out messages')
y = MarcinsMessenger(name='Receive messages')

x.start()
y.start()
