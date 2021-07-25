import ez
import json
import requests

def get_from_url():
	# url="https://music.163.com/api/playlist/detail?id=595556898"
	url="https://api.imjad.cn/cloudmusic/?type=playlist&id=595556898"
	response=json.loads(requests.get(url).text)
	print (json.dumps(response,indent=4))

class mouse():
	def scroll():

	def open_file_location():

class keyboard():
	def copy_path():

class file():
	def move(original_path,new_path):

	def get_name(path):

if __name__ == '__main__':
	