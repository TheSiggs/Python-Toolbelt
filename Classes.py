import threading


class Enemy:
    life = 3
    gender = 'female'

    def __init__(self, x, name):
        self.energy = x
        self.name = name

    def get_energy(self):
        print(self.energy)

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life), 'life left')


# -----------
# Inheretance
# -----------
class Parent():

    def print_last_name(self):
        print('Siggs')


class Child(Parent):

    def print_first_name(self):
        print('Sam')


# --------------------
# Multiple Inheritence
# --------------------
class Mario():
    def move(self):
        print('Moving')


class Shroom():
    def eat_shroom(self):
        print('I have Grown')


class BigMario(Mario, Shroom):
    pass


# ---------
# Threading
# ---------
class SamsMessenger(threading, Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = SamsMessenger(name='Send Messages')
y = SamsMessenger(name='Recieve Messages')
x.start()
y.start()
