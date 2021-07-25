import pyperclip
import shutil
import os
import keyboard
import time
import ez

print("Number of songs needed to move = ",end="")
numer_of_songs=int(input())

for i in range(numer_of_songs):
	ez.check_force_stop()

	print (i+1)

	#open everything
	keyboard.send("ctrl+alt+f")
	ez.time.sleep(0.8)

	ez.check_force_stop()

	#find the repeated songs
	path="E:\\Data\\Music\\网易云音乐\\";
	keyboard.write(path+" (1)")

	##get the name of the songs
	keyboard.send("down")
	ez.time.sleep(0.5)
	keyboard.send("f2")
	ez.time.sleep(0.5)
	keyboard.send("ctrl+a")
	ez.time.sleep(0.5)
	keyboard.send("ctrl+c")
	ez.time.sleep(0.5)

	#find the actual name of the song
	repeated_name=pyperclip.paste()
	original_name=repeated_name.replace(" (1)","")
	print (original_name)

	#move the repetead file
	source=path+repeated_name
	if (os.path.isfile(source)):
		destination="C:\\Users\\User\\Desktop\\1\\repeated\\"+repeated_name
		shutil.move(source,destination)
		print ("repeated file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...repeated file not found (⊙_⊙)?")

	#move the original file
	source=path+original_name
	if (os.path.isfile(source)):
		destination="C:\\Users\\User\\Desktop\\1\\original\\"+original_name
		shutil.move(source,destination)
		print ("original file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...original file not found (⊙_⊙)?")

	print()

print ("done ヾ(￣▽￣)")