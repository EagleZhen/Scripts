import pyperclip
import shutil
import os
import keyboard
import time
import ez

path="C:\\Data\\Music\\网易云音乐\\";

print ("Hint: If the file name is like \"五月天 - 明日 (1)\" then input 1")
no_of_repeat = " ("+input("Number of repeat (1,2,3) = ")+")"

#open everything
keyboard.send("ctrl+alt+f")
time.sleep(0.5)

#input path
keyboard.write(path+no_of_repeat)
time.sleep(1)

# focus on the search result
keyboard.send("ctrl+f")
keyboard.send("down")
time.sleep(0.5)

# copy the paths of all the files
keyboard.send("ctrl+a")
keyboard.send("ctrl+shift+c")
time.sleep(0.5)

file_list = pyperclip.paste().split("\r\n")

for file in file_list:
	ez.check_force_stop()

	# find the actual name of the song without (1)
	repeated_file_path=file
	original_file_path=repeated_file_path.replace(no_of_repeat,"")
	print (original_file_path)

	#move the repetead file
	source=repeated_file_path
	if (os.path.isfile(source)):
		destination="C:\\Data\\Cache\\Temp\\repeated\\"
		ez.move_file(source,destination)
		print ("repeated file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...repeated file not found (⊙_⊙)?")

	#move the original file
	source=original_file_path
	if (os.path.isfile(source)):
		destination="C:\\Data\\Cache\\Temp\\original\\"
		ez.move_file(source,destination)
		print ("original file is moved ヾ(￣▽￣)")
	else:
		print ("hmm...original file not found (⊙_⊙)?")

	print("*******************************")

	# time.sleep(1)

print ("done ヾ(￣▽￣)")