import json
import ez
import os
import shutil

# f = open("./sample.json")
# sample = json.load(f)
# key_list = list(sample.keys())
# print (key_list)

j4_data_path = f"{os.path.dirname(__file__)}/j4/EITP_S5(1)_Python"
j7_data_path = f"{os.path.dirname(__file__)}/j7"
j7_id = 2100
total_case = 0
final_json = ""

for j4_id in range(8001,8017):
	print (j7_id)

	file_name = f"{j4_data_path}/{str(j4_id)}/problem.json"
	# print (f"{j4_id} : {file_name}")

	# copy data files
	j4_case_path = f"{j4_data_path}/{str(j4_id)}/testcase"

	for filename in os.listdir(j4_case_path):
		j4_file = f"{j4_case_path}/{filename}"
		j7_file = f"{j7_data_path}/{j7_id}/{j7_id}_{int(filename.split('.')[0])-1:02d}.{filename.split('.')[1]}"
		# print(j4_file," ===> ", j7_file)
		
		# make new directories
		os.makedirs(f"{j7_data_path}/{j7_id}",exist_ok=True)
		shutil.copyfile(j4_file, j7_file)

		total_case = int(filename.split('.')[0])
	
	f = open(file_name)
	old_data = json.load(f)

	new_data = {}
	# for key,value in old_data.items():
	# 	print (f"{key} : {value}")

	# print (j7_id, old_data["test_case_score"])

	new_data["id"] = j7_id
	new_data["name"] = old_data["title"]
	new_data["timeLimit"] = old_data["time_limit"]
	new_data["type"] = "traditional"
	new_data["hidden"] = True
	new_data["releaseDate"] = "0000-00-00"
	new_data["author"] = ""
	new_data["statement"] = f'{old_data["description"]["value"]}\n\n### Input\n\n{old_data["input_description"]["value"]}\n\n### Output\n\n{old_data["output_description"]["value"]}'
	new_data["sampleTests"] = old_data["samples"]
	new_data["notes"] = old_data["hint"]["value"]
	new_data["showTutorial"] = False
	new_data["tutorial"] = ""
	new_data["solutionLanguage"] = "C++"
	new_data["solution"] = ""
	new_data["specialJudge"] = ""
	new_data["enableSubtask"] = False
	new_data["caseCount"] = total_case
	new_data["subtasks"] = [{"score": 100,"depends": [],"cases": []}]
	new_data["solveCount"] = 0
	new_data["accessibleUsers"] = []

	f.close()

	final_json += json.dumps(new_data, indent=4) + "\n"

	j7_id += 1

with open(f"{j7_data_path}/j7.json", 'w') as file:
	file.write(final_json)