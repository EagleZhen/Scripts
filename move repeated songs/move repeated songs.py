import pyperclip
import shutil
import os
import keyboard
import time
import ez

path="E:\\Data\\Music\\网易云音乐\\";
no_of_repeat = " (2)"

print("Number of songs needed to move = ",end="")

#open everything
keyboard.send("ctrl+alt+f")
time.sleep(0.5)

#input path
keyboard.write(path+no_of_repeat)
time.sleep(1)

# show the number of songs
numer_of_songs=int(input())

# focus on everything
keyboard.send("ctrl+alt+f")
time.sleep(1)

for i in range(numer_of_songs):
	ez.check_force_stop()

	print (i+1)

	# force stop the program
	ez.check_force_stop()

	# select the first result
	keyboard.send("ctrl+f")
	keyboard.send("down")
	time.sleep(0.5)

	# copy the full name of the file
	keyboard.send("ctrl+shift+c")
	time.sleep(0.5)

	# find the actual name of the song without (1)
	repeated_name=pyperclip.paste().replace("\"","")
	original_name=repeated_name.replace(no_of_repeat,"")
	print (original_name)

	#move the repetead file
	source=repeated_name
	if (os.path.isfile(source)):
		destination="E:\\Data\\Cache\\Downloads\\repeated\\"
		ez.move_file(source,destination)
		print ("repeated file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...repeated file not found (⊙_⊙)?")

	#move the original file
	source=original_name
	if (os.path.isfile(source)):
		destination="E:\\Data\\Cache\\Downloads\\original\\"
		ez.move_file(source,destination)
		print ("original file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...original file not found (⊙_⊙)?")

	print("*******************************")

	time.sleep(1)

print ("done ヾ(￣▽￣)")