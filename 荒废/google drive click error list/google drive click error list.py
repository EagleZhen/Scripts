import keyboard
import mouse
import ez
import time

n=int(input("Number of items = "))

mouse.move(425,165)
mouse.click()
# print ("clicked")

keyboard.send("tab")
time.sleep(0.1)
keyboard.send("tab")
time.sleep(0.1)

for i in range(0,n):
    ez.check_force_stop()
    keyboard.send("tab+enter")
    time.sleep(0.2)
    keyboard.send("down+enter")
    time.sleep(0.2)