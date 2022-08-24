from keyboard import press,release,send
from time import sleep

# wait_time = 4
wait_time = 5.3

# switch to gta 5 window
sleep(1)
send("alt+tab")
sleep(1)

#join the lucky draw
press("E")
sleep(1)
release("E")
print ("E")

#adjust force
sleep(wait_time)

#spin the wheel
press("S")
sleep(1)
release("S")
print("S")