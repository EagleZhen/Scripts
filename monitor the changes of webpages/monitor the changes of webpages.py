import requests
import time
import hashlib
import urllib
import ez
import datetime

first_time=True
current_hash=0
previous_hash=0

while(True):
	url = "https://atcoder.jp/"
	response = urllib.request.urlopen(url).read()

	if (first_time):
		current_hash = previous_hash = hashlib.sha224(response).hexdigest()
		first_time=False
	else:
		current_hash = hashlib.sha224(response).hexdigest()
	
	if (current_hash!=previous_hash):
		ez.random_play_song()
		previous_hash=current_hash

	print ("\rsame",datetime.datetime.now(),sep="",end="")
	
	time.sleep(600)