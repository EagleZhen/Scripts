from keyboard import send,write
from time import sleep
from ez import check_force_stop

sleep(5)

with open("link.txt") as f:
	for line in f.readlines():
		print (line)
		line = line.strip()
		send("ctrl+t")
		sleep(1)
		write(line)
		send("enter")
		sleep(1)
		check_force_stop()

	