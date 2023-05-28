import os,shutil

def move_file(source_file_path, destination_path):
	perform_file_operation(source_file_path, destination_path, shutil.move)

def copy_file(source_file_path, destination_path):
	perform_file_operation(source_file_path, destination_path, shutil.copy)

def perform_file_operation(source_file_path, destination_path, file_operation):
	if not os.path.exists(source_file_path):
		print(f"Error: Source file '{source_file_path}' does not exist.")
		return
		
	if not os.path.exists(destination_path):
		print(f"Error: Destination path '{destination_path}' does not exist.")
		return
	
	# os.path.basename(): extracts the base name of the file from the path
	destination_file_path = os.path.join(destination_path, os.path.basename(source_file_path))
	
	# file with the same name already exists in the destination path
	if (os.path.exists(destination_file_path) and os.path.isfile(destination_file_path)):
		user_input = input(f"Warning: File '{destination_file_path}' already exists. Do you want to overwrite it? (yes/no): ")
		
		if user_input.lower() != 'yes':
			print("Operation aborted by user.")
			return
		
	try:
		file_operation(source_file_path, destination_file_path)

		# rename the operation name to fit into the prompt sentence
		operation_name = file_operation.__name__.split('.')[-1]
		if (operation_name=="copy"):
			operation_name_passive="copied"
		else:
			operation_name_passive="moved"

		print(f"File '{source_file_path}' {operation_name_passive} to '{destination_file_path}' successfully.")
	except Exception as e:
		print(f"Error: Failed to {operation_name} file '{source_file_path}' to '{destination_file_path}'.")
		print(e)

if __name__ == '__main__':
	source = "C:/Users/EZ/Desktop/test/james.txt"
	dest = "C:/Users/EZ/Desktop/test/dest"
	move_file(source,dest)
