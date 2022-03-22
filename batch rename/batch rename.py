import os

root_path=input("Diretory = ")+"\\"
file_list = os.listdir(root_path)
# print (file_list)

for file in file_list:
	# file (start,end]
	prefix=file[:4]
	suffix=file[-4:]
	if (suffix == ".pdf") :
		# print(file, " -> ", prefix+suffix)
		os.rename(root_path+file , root_path+prefix+suffix)