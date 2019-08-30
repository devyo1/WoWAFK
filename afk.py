import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller
import time
import random


keyboard = Controller()
space = Key.space
left = Key.left
right = Key.right
down = Key.down
keys = [space, left, right, down]

def main():
    for a in range(5000, 0, -1):
        result = str(a)+(" Jumps Left")

        print(result)


        time.sleep(zz)
        jump()

zz = random.randint(350,750)

def jump():
    keyboard.press(space)
    print("You Jumped")
    keyboard.release(space)


main()

#
