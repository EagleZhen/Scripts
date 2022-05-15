import time
import ez
import os

f = open('list.txt','r')
source_path=f.readline().rstrip()+"\\"
destination_path=f.readline().rstrip()+"\\"
file_list=os.listdir(source_path)

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
		# print(source_path+file,"\n-> ",destination_path+location)
		ez.move_file(source_path+file,destination_path+location)

