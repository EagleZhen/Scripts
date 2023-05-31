import os
from itertools import islice
from ez import get_info_path,stop,pause

root_path = os.getcwd()
info_path = get_info_path()
# stop(info_path)
device_list = []

class software:
	def __init__(self, name, version, command):
		self.name = name
		self.version = version
		self.command = command.replace("<name>",self.name) # replace with the software name (e.g. scrcpy,sndcpy)

	def path(self):
		# return f"{root_path}\\{self.name}{self.version}\\"
		return os.path.join(root_path, self.name+self.version)

	def connect(self,id,name=None):
		os.chdir(self.path())
		os_command = self.command.replace("<title>",f"\"{name}\"") # replace with the device name
		os_command = os_command.replace("<id>",id) # replace with the device id
		pause (os_command)
		os.system(os_command)

scrcpy = software("scrcpy","2.0", "start <name>-noconsole.vbs -s <id> --window-title <title> --window-borderless --no-clipboard-autosync --fullscreen")
# print(scrcpy.command)
sndcpy = software("sndcpy","1.1", "start <name> <id>")

class device:
	def __init__(self, name, ip, ip_id, port, serial, connection_type, video, audio):
		self.name				= name
		self.ip					= ip[int(ip_id)]
		self.port				= port
		self.serial				= serial
		self.connection_type	= connection_type
		self.video				= bool(int(video))
		self.audio				= bool(int(audio))
		self.id					= serial # to specify devices

	def print_info(self):
		# method 1
		for attribute, value in self.__dict__.items():
			print (f"{attribute:15} : {value}")

		# method 2
		# for attribute in vars(self):
		# 	print (f"{attribute} : {vars(self)[attribute]}")
	
	def adb_connect(self):
		print("Connecting adb...");
		if (self.connection_type=="WIFI"):
			# Use IP instead of serial number to specify devices (Wireless connection)
			self.id = f"{self.ip}:{self.port}"
			os.system(f"adb connect {self.id}")
		else:
			# Use serial number to specify devices (Wired connection)
			self.id = f"{self.serial}"

	def share_screen(self):
		if (self.video):
			print("Sharing screen...");
			scrcpy.connect(self.id, self.name)
	
	def share_audio(self):
		if (self.audio):
			print("Sharing audio...");
			sndcpy.connect(self.id, self.name)

def read_device_info():
	with open(os.path.join(info_path,"Device Info.txt"), 'r') as file:
		variable_name = []
		for i,line in enumerate(file):
			if (i==0):
				variable_name = list(map(str.strip,line.split('|')))
			else:
				device_info = list(map(str.strip,line.split('|')))
				device_info[1] = device_info[1].split(";")
				# print(device_info)
				command = "device_list.append(device("+str(device_info)[1:-1]+"))"
				# print(command)
				exec(command)
	
read_device_info()
for i,item in enumerate(device_list):
	print(f"{'='*18}{i}{'='*10}") # print with alignment
	item.print_info()

device_id = int(input("Device ID = "))

device_list[device_id].adb_connect()

device_list[device_id].share_screen()

device_list[device_id].share_audio()