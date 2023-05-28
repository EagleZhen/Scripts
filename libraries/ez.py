# sys.path.append() to add this module into the serach path list of python

import time
import sys
import keyboard
import os
import tqdm
import shutil
import subprocess

# 按住大写键停止程序
def check_force_stop():
	if (keyboard.is_pressed('capslock')):
		sys.exit("\aSir, I have stopped the program for you.")

def timer(total_seconds):
	print ("Start countdown from: ",int(total_seconds/60),":",int(total_seconds%60),sep="")

	second=total_seconds
	for i in tqdm.trange(int(total_seconds)):
		second-=1
		#print ("\r",int(second/60),":",int(second%60),sep="",end="")
		time.sleep(1)

# 移动文件，前面是file，后面是folder
def move_file(source,destination):
	if (os.path.exists(source)):
		os.makedirs(destination,exist_ok=True)
		shutil.move(source,destination)
		print ("================\n",source, "\nhas been moved to\n",destination,"\n================")
	else:
		print (source + " not exist")

# 复制文件，前面是file，后面是folder
# 如果同名会覆盖
def copy_file(source,destination):
	if (os.path.exists(source)):
		os.makedirs(destination,exist_ok=True)
		shutil.copy(source,destination)
		print ("================\n",source, "\nhas been copied to\n",destination,"\n================")
	else:
		print (source + " not exist")

def pause(message=None):
	print (message)
	os.system("pause")

def get_repository_name():
	try:
		# get the repository url from local git config file
		output = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
		# convert bytes to string and split by '/'
		url_parts = output.decode().strip().split('/')
		repository_name = url_parts[-1].replace('.git', '')
		return repository_name
	
	# if any exception of these types is raised during execution, the corresponding except block will handle it
		# subprocess.CalledProcessError
			# execute a command that does not exist
			# i.e. git is not yet installed
		# IndexError
			# try to access an index that is out of range
			# unlikely to happen, but still may happen in "url_parts[-1]"
	except (subprocess.CalledProcessError, IndexError):
		return None

# get the corresponding info folder for each script
# assume
	# the name of the info folder is "info for program"
	# the name of the corresponding folder inside info folder is the same as the script file name
def get_info_path(program_file_path):
	git_repo_name = get_repository_name()
	info_folder = "info for program"
	# get the root path of the git repository
	root,script_folder = program_file_path.split(f"\\{git_repo_name}")
	script_folder = script_folder[1:] # remove the '\' at the beginning
	if (script_folder==""): # when the script is in the root folder
		script_folder = root

	# pause("root: "+root)
	# pause("script: "+script_folder)

	info_path = f"{root}\\{git_repo_name}\\{info_folder}\\{script_folder}"

	return info_path