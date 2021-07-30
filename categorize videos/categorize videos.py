import time
import ez
import os

root_path="E:/Data/Videos/Bandicam/"
file_list=os.listdir(root_path);

location_dict={
	"Celeste": "Celeste",
	"UNDERTALE": "Undertale",
	"GTA5": "GTA 5",
	"GenshinImpact": "Genshin Impact",
	"Obduction-Win64-Shipping": "Obduction",
	"ChildofLight": "Child of Light",
	"Spectrum": "Spectrum"	
}

for file in file_list:
	prefix=file.split(" ",1)[0]
	# print (prefix)
	if (prefix in location_dict):
		location=location_dict[prefix]
		# print(location)
		ez.move_file(root_path+file,root_path+"Games/"+location)

