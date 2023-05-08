from keyboard import press,release,send
from time import sleep

# wait_time = 4
# wait_time = 5.6 # cloth
# wait_time = 6 # 40000 money
# wait_time = 5.9 # 15000 money

# wait_time = 5.98 # mystery
wait_time = 4.15

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