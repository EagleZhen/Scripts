import subprocess
from ez import pause

def get_github_repository_name():
	try:
		# get the repository url from local git config file
		output = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
		# convert bytes to string and split by '/'
		url_parts = output.decode().strip().split('/')
		
		pause(output)
		pause(output.decode())
		
		# get the last part of the url and remove the '.git' extension
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

# Usage
repository_name = get_github_repository_name()
if repository_name:
	print("GitHub Repository Name:", repository_name)
else:
	print("Unable to retrieve GitHub repository name.")
