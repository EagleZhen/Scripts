from time import sleep
from keyboard import press, release, is_pressed

while (True):
    if (is_pressed("HOME")):
        release("CAPSLOCK")
        press("CAPSLOCK")
        print("Activated\a")
    sleep(1)