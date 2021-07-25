import time
import sys
import keyboard
import mouse
import pyperclip
import subprocess
import os
import random
import tinytag
import tqdm

def check_force_stop():
	if (keyboard.is_pressed('capslock')):
		sys.exit("\aSir, I have stopped the program for you.")

def timer(total_seconds):
	print ("Start countdown from: ",int(total_seconds/60),":",int(total_seconds%60),sep="")

	second=total_seconds
	for i in tqdm.trange(int(total_seconds)):
		second-=1
		#print ("\r",int(second/60),":",int(second%60),sep="",end="")
		time.sleep(1)

def random_play_song():
	path="E:/Data/Music/网易云音乐/"
	file_list=os.listdir(path)

	song=""
	while (song.find(".mp3")==-1):
		song=random.choice(file_list)

	#open in netease cloud music
	os.startfile(path+song)
	# subprocess.Popen(["D:/Program Files/QQPlayer/QQPlayer.exe",path+song])

	info=tinytag.TinyTag.get(path+song)
	print (song,"\n============================")

	timer(info.duration)
	#stop the netease cloud music
	keyboard.send("ctrl+alt+space")
	# os.system("taskkill /f /im QQPlayer.exe")

def move_file(source,destination):
	shutil.move(source,destination)