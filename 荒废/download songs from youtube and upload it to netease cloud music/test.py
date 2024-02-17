import requests
import json

def get_song_info()
	response=requests.get("https://musicapi.leanapp.cn/song/detail?ids=440241201")
	s=response.json()

	# song_num=0
	for song in s["songs"]:
		#name of the song
		song_name=song["name"]

		# song_num+=1
		# print ("Song #",song_num,": ",song["name"],sep="",end="\n")

		artist=[]
		for artist in song["ar"]:
			artist_name=artist["name"]

			# artist_num+=1;
			# print ("Artist #",artist_num,": ",artist["name"],sep="",end="\n")

		# print ("Album: ",song["al"]["name"],sep="",end="\n")

def get_song_info()
	


