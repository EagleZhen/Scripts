import ez
import webbrowser

subtask_score=[]
subtask_case=[]
subtask_cnt=0
case_cnt=0
task_id=0

f=open("j2.txt","r")
# task_id=input("task_id = ")
task_id=f.readline().rstrip()
print ("Task",task_id)

def from_j2():
	global subtask_score,subtask_case,subtask_cnt

	# subtask_string=input("Distribution of subtask in J2 = ")
	subtask_string=f.readline().rstrip()
	subtask_split=subtask_string.split(",")

	# for i in subtask_split:
	# 	print (i)

	subtask_cnt=int(subtask_split[0])
	for i in range(1,len(subtask_split),2):
		# print (subtask_split[i],subtask_split[i+1])
		subtask_score.append(int(subtask_split[i]))
		subtask_case.append(int(subtask_split[i+1]))

	global case_cnt
	for i in subtask_case:
		case_cnt+=i
	print ("Number of Cases:",case_cnt)

def to_j8():
	#focus on the chrome window
	ez.mouse.move(1523,714)
	ez.mouse.click()
	ez.time.sleep(0.5)

	ez.keyboard.send("ctrl+t")
	ez.keyboard.send("ctrl+l")
	ez.time.sleep(0.5)
	ez.keyboard.write("http://210.176.23.169:3000/edit-task/" + task_id + "/edit-data")

	# print("http://210.176.23.169:3000/edit-task/" + task_id + "/edit-data")

	ez.keyboard.send("enter")
	ez.time.sleep(8)

	######################
	ez.check_force_stop()
	######################

	#switch on subtask button
	for i in range(0,12):
		ez.keyboard.send("tab")
		ez.time.sleep(0.0001)
	for i in range(0,case_cnt*3):
		ez.keyboard.send("tab")
		ez.time.sleep(0.0001)

	ez.time.sleep(2)

	######################
	ez.check_force_stop()
	######################

	ez.keyboard.send("space")

	#move to the add subtask button
	for i in range(0,5):
		ez.keyboard.send("tab")
	ez.time.sleep(0.5)

	# add subtask
	for i in range(0,subtask_cnt-1):
		ez.keyboard.send("enter")
	ez.time.sleep(0.5)

	#input subtask information
	for i in range(0,subtask_cnt*4):
		ez.keyboard.send("shift+tab")
	ez.keyboard.send("tab")
	ez.time.sleep(0.5)

	partial_sum=0
	for i in range(0,subtask_cnt):
		ez.keyboard.write(str(subtask_score[i]))
		ez.keyboard.send("tab")
		ez.keyboard.send("tab")
		
		ez.keyboard.write(str(partial_sum) + "-" + str(partial_sum+subtask_case[i]-1))
		partial_sum+=subtask_case[i]

		ez.keyboard.send("tab")
		ez.keyboard.send("tab")

	#save
	ez.keyboard.send("enter")
	ez.time.sleep(0.5)

	######################
	ez.check_force_stop()
	######################

	#open statement window
	ez.mouse.move(526,1708)
	ez.mouse.click()
	ez.time.sleep(0.5)

	ez.keyboard.send("ctrl+t")
	ez.keyboard.send("ctrl+l")
	ez.time.sleep(0.5)

	ez.keyboard.write("http://210.176.23.169:3000/task/" + task_id)
	ez.keyboard.send("enter")
	ez.time.sleep(0.5)

	######################
	ez.check_force_stop()
	######################

	ez.keyboard.send("ctrl+l")
	ez.time.sleep(0.5)
	ez.keyboard.write("http://210.176.23.169:3000/task/" + task_id + "#output")
	ez.keyboard.send("enter")

	#move back to the first depend
	ez.mouse.move(265,725)
	ez.mouse.click()

	for i in range(0,subtask_cnt*4):
		ez.keyboard.send("shift+tab")
	ez.keyboard.send("tab")
	ez.keyboard.send("tab")
	ez.time.sleep(0.5)

	######################
	ez.check_force_stop()
	######################

from_j2()
to_j8()

# ez.mouse.drag(684,14, 684,1050, absolute=True,duration=0.25)
# ez.mouse.double_click()