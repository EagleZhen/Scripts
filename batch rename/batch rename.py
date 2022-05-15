import os

root_path=input("Diretory = ")+"\\"
file_list = os.listdir(root_path)
# print (file_list)

def rename(org,des):
	os.rename(root_path+org , root_path+des)

def marking_student_no():
	# 就是将samsung note改完答案export出来的笔记，重新命名为学号
	for file in file_list:
		# syntax format: file (start,end]

		#file name
		prefix=file[:4]
		#extension name
		ext=file[-4:]
		if (ext == ".pdf"):
			print(file, " -> ", prefix+ext)
			rename(file , prefix+ext)

def bilibili_subtitles():
	# 用bilibili下载下来的字幕文件名，把同文件夹下的mp4资源命名
	dict={}

	for file in file_list:
		ext=file[-4:]
		if (ext == ".ass"):
			file_name=file[:-4]
			# print (file_name)

			number=file[:file.find('.')]
			leading_zero=""
			for i in range(0,2-len(number)):
				leading_zero=leading_zero+"0";
			number=leading_zero+number
			# print (number)

			dict[number]=file_name
			

	for file in file_list:
		ext=file[-4:]
		if (ext == ".mp4"):
			number=file[14:16]
			# print (number)

			if number in dict:
				print(file, " -> ", dict[number]+ext)
				rename(file , dict[number]+ext)

def remove_bandicam_prefix():
	#将以前旧的bandicam录像文件的前缀bandicam删掉，和obs studio统一
	for file in file_list:
		prefix=file[:8]
		if (prefix == "bandicam"):
			new_name = file.replace("bandicam","")
			print(file, " -> ", new_name)
			rename(file , new_name)
	
if __name__ == "__main__":
	remove_bandicam_prefix()