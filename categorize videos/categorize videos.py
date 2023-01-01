import time
import ez
import os

f = open('List.txt','r')
source_path=f.readline().rstrip()+"\\"
destination_path=f.readline().rstrip()+"\\"
file_list=os.listdir(source_path)

location_dict={}

for line in f:
	video_name = line.split('|')[0].strip()
	folder_name = line.split('|')[1].strip()
	# print(video_name," - ", folder_name,sep="")
	location_dict[video_name]=folder_name

for file in file_list:
	prefix = file.split(' ')[0]
	friend = file.split(' ')[1]
	# print("wtffffffff",friend)

	# print (prefix)
	if (prefix in location_dict):																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
		location=location_dict[prefix]

		full_destination_path = f"{destination_path}{location}"

		# play with friends
		if (friend!="S"):
			full_destination_path+="\\with friends"
		
		# single player
		else:
			new_file = file.replace("S ","")
			os.rename(source_path+file, source_path+new_file)

		# print(source_path+file,"\n-> ",full_destination_path)

		print (f"...... Moving \"{new_file}\" ......")
		ez.move_file(source_path+new_file,full_destination_path)

print("\a")
os.system("pause")