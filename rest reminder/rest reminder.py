import time
import os
import random
import keyboard
import ez
import subprocess

def random_play_song():
	path="E:/Data/Music/网易云音乐/"
	file_list=os.listdir(path)

	song=""
	while (song.find(".mp3")==-1):
		song=random.choice(file_list)

	# os.startfile(path+song)
	subprocess.Popen(["C:/Apps/QQPlayer/QQPlayer.exe",path+song])
	print(song)

	time.sleep(300)
	os.system("taskkill /f /im QQPlayer.exe")

	# keyboard.send("alt+tab")
	# choice=int ( input("0:ok | 1:next song | 2:I don't wanna rest yet\n") )

	
	# if (choice==0):
	# 	keyboard.send("alt+tab")
	# 	time.sleep(0.5)
	# 	keyboard.send("windows+down")
	# 	keyboard.send("windows+down")

	# elif (choice==1):
	# 	os.system("taskkill /f /im QQPlayer.exe")
	# 	random_play_song()

	# elif (choice==2):
	# 	os.system("taskkill /f /im QQPlayer.exe")

def timer():
	total_minutes=int( input("minutes = ") )

	# keyboard.send("windows+d")
	while(True):
		for minutes in range(total_minutes):
			print (total_minutes-minutes," minutes left! Please add oil!",sep="")
			time.sleep(60)

			# for seconds in range(60):
			# 	print (total_minutes-minutes-1,":",59-seconds,sep="")
			# 	time.sleep(1)

		random_play_song()

timer()
# random_play_song()