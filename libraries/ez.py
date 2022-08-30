# sys.path.append() to add this module into the serach path list of python

import time
import sys
import keyboard
import os
import random
import tqdm
import shutil

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