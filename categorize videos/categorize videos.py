import ez,os,json
from ez import pause,stop,rename_file
from os.path import join
from tqdm import tqdm

# stop(ez.get_info_path())
info_file_path = join(ez.get_info_path(),"List.json")
# stop(info_file_path)

with open(info_file_path,'r') as f:
	data = json.load(f)

source_path=data["source_path"]
destination_path=data["destination_path"]
file_list=os.listdir(source_path)

location_dict=data["aliases"]
# stop(location_dict)

change_list = [] # list of files to be moved and their corresponding destination path
for file in file_list:
	# assume the file name format is "<prefix> <friend> <original file name>" 
	prefix = file.split(' ')[0] # the game alias
	friend = file.split(' ')[1] # whether play with friends or single player

	if (prefix in location_dict):
		final_destination_path = join(destination_path, location_dict[prefix])

		# single player
		if (friend=="F"):
			new_file = file.replace("F ","")
			final_destination_path = join(final_destination_path, "with friends")
		
		# play with friends
		elif (friend=="S"):
			new_file = file.replace("S ","")
		
		else:
			print (f"[!] \"{file}\" is not yet labelled.")
			continue
		
		source = join(source_path,file)
		dest = join(final_destination_path,new_file)
		change_list.append((source,dest))

current_prefix = ""
for source,dest in change_list:
	# stop(source,dest)
	prefix = os.path.basename(source).split(' ')[0]
	if (prefix != current_prefix):
		current_prefix = prefix
		print(f"=====================================\n{location_dict[current_prefix]}\n")
	print(f"\"{source}\" -> \"{dest}\"")

if (len(change_list)==0):
	print("No files to be moved.")
	quit()

choice = input("=====================================\nCorrect? (yes/no): ")
if (choice == "yes"):
	total_size = 0
	for source,dest in change_list:
		total_size += os.path.getsize(source)

	progress_bar = tqdm(total=total_size, unit="B")
	processed_size = 0

	# update the progress bar whenever a file is moved
	for source,dest in change_list:
		rename_file(source, dest)
		progress_bar.update(os.path.getsize(dest))

print("\a")