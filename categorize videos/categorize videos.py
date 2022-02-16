import time
import ez
import os

f = open('list.txt','r')
root_path=f.readline().strip()
file_list=os.listdir(root_path);

location_dict={}

for line in f:
	video_name = line.split('|')[0].strip()
	folder_name = line.split('|')[1].strip()
	# print(video_name," - ", folder_name,sep="")
	location_dict[video_name]=folder_name

# os.system("pause")

for file in file_list:
	prefix=file.split(" ",1)[0]
	# print (prefix)
	if (prefix in location_dict):
		location=location_dict[prefix]
		# print(location)
		ez.move_file(root_path+file,root_path+"Games/"+location)

