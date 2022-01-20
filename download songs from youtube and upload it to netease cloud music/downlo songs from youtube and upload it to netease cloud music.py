import ez
import mouse
import keyboard

import requests
import json

import webbrowser
import time

import pyperclip

song_name=""
artist_name=[]
album_name=[]

youtube_url=""
netease_url=""

def get_song_info():
	global song_name,artist_name,album_name,netease_url

	song_id=netease_url.replace("http://music.163.com/song?id=","")
	song_id=song_id.replace("&userid=417214757","")

	response=requests.get("https://musicapi.leanapp.cn/song/detail?ids="+song_id)
	s=response.json()

	for song in s["songs"]:

		#name of the song
		song_name=song["name"]
		print ("Song: ",song_name,sep="",end="\n")

		artist=[]
		artist_num=0
		for artist in song["ar"]:
			artist_num+=1;

			#names of multiple artists
			artist_name.append(artist["name"])
			print ("Artist #",artist_num,": ",artist["name"],sep="",end="\n")

		print ("Album: ",song["al"]["name"],sep="",end="\n")


def download_from_youtube():
	global youtube_url

	y2_url="y2 "+youtube_url.replace("https://youtu.be/","")

	webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("D:/Program Files/Chrome/App/chrome.exe"))

	#go to chrome
	webbrowser.get("chrome").open_new("")
	time.sleep(3)
	keyboard.send("windows+up")

	ez.check_force_stop()

	#go to y2mate
	keyboard.send("ctrl+l")
	keyboard.write(y2_url)
	keyboard.send("enter")
	time.sleep(3)

	#click "mp3"
	mouse.move(850,510)
	mouse.click()
	time.sleep(1)

	#click the first download button
	mouse.move(1066,654)
	mouse.click()
	time.sleep(15)

	#click the second download button
	mouse.move(715,270)
	time.sleep(1)
	mouse.click()
	time.sleep(3)

	ez.check_force_stop()

	#pop up the file explorer window
	keyboard.send("ctrl+l")
	keyboard.write("C:/Users/User/Desktop/")
	keyboard.send("enter")
	time.sleep(1)

	#focus on the file name
	mouse.move(486,621)
	mouse.click()
	time.sleep(1)

	#type the file name
	first_item=True;
	for artist in artist_name:
		if (first_item):
			first_item=False
		else:
			keyboard.write(',')

		keyboard.write(artist)

	keyboard.write(" - "+song_name)
	keyboard.send("enter")
	time.sleep(1)
	keyboard.send("left")
	keyboard.send("enter")

f = open("url.txt", "r")
n=int(f.readline())
print (n)

for i in range(n):
	youtube_url=f.readline().rstrip("\n")
	netease_url=f.readline().rstrip("\n")
	f.readline()

	print (youtube_url),
	print (netease_url)

	get_song_info()
	download_from_youtube()