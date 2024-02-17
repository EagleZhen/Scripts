from keyboard import press,release,send,wait
from time import sleep

wait_time = 4

# switch to gta 5 window
sleep(1)
send("alt+tab")
sleep(1)

#join the lucky draw
press("E")

#spin the wheel
press("S")
sleep(1)
release("S")
print("S")