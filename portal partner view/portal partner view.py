from time import sleep
from keyboard import press, release, is_pressed

cnt = 0
while (True):
    if (is_pressed("END")): # End key to stop the script
        print("Script stopped\a")
        release("CAPSLOCK")
        break
        
    release("CAPSLOCK")
    press("CAPSLOCK")
    print("Reactivated")
    cnt = 0
        
    sleep(5)