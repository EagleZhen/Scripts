import os
from sys import setswitchinterval
import eyed3

def rename():
	for name in change_list:
		print(f"\"{name}\" -> \"{change_list[name]}\"")

	confirm = input("Correct? (Type \"yes\" if correct) = ")
	if (confirm == "yes"):
		for name in change_list:
			os.rename(root_path+name , root_path+change_list[name])

def marking_student_no():
	# 就是将samsung note改完答案export出来的笔记，重新命名为学号
	for file in file_list:
		# syntax format: file (start,end]

		#file name
		prefix=file[:4]
		#extension name
		ext=file[-4:]
		if (ext == ".pdf"):
			change_list[file]=prefix+ext

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
				change_list[file]=dict[number]+ext

def replace_substring_to_specified_substring():
	# 替换每个文件名的特定字符串，或者在前后插入特定字符串
	old_str = input("The substring to be replaced ( any substring / *front / *back ) = ")
	new_str = input("Replace the substring to = ")

	for file in file_list:
		#do not make changes to the file extension

		# ext_dot_pos=file.rfind(".")
		# ext=file[ext_dot_pos:]
		# name=file[:ext_dot_pos]

		#更简洁写法
		name = os.path.splitext(file)[0]
		ext = os.path.splitext(file)[1]

		# print (name, " | ", ext)

		#add as prefix
		if (old_str == "*front"):
			new_name = new_str + name
			change_list[file]=new_name+ext
		#add as suffix
		elif (old_str=="*back"):
			new_name = name+new_str
			change_list[file]=new_name+ext

		#replace an existing substring
		elif (name.find(old_str)!=-1):
			new_name = name.replace(old_str,new_str)
			change_list[file]=new_name+ext

def mp3_rename():
	# 将mp3文件名改成 artist - song name 格式

	for file in file_list:
    	# print (os.path.splitext(file))
		if (os.path.splitext(file)[1]==".mp3"):
			audio_file=eyed3.load(root_path+file)
			
			artist=audio_file.tag.artist
			artist=artist.replace("/",",")

			title=audio_file.tag.title
			title=title.replace("/"," ")

			new_name=artist+" - "+title+".mp3"
			new_name=new_name.replace("?","？")

			# check name conflicts
			if (os.path.exists(root_path+new_name)==0):
				change_list [file] = new_name
			else:
				print(f"filename conflicts: \"{file}\" ")
	
if __name__ == "__main__":
	root_path=input("Diretory = ")+"\\"
	file_list = os.listdir(root_path)
	# print (file_list)
	change_list = {}

	print ("1: 用bilibili下载下来的字幕文件名，把同文件夹下的mp4资源命名")
	print ("2: 将mp3文件名改成 artist - song name 格式")
	print ("3: 替换每个文件名的特定字符串，或者在前后插入特定字符串")
	id = int(input())
	
	if (id==1): bilibili_subtitles()
	elif (id==2): mp3_rename()
	elif (id==3): replace_substring_to_specified_substring()

	rename()