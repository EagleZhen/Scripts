import os
from ez import get_repository_name,get_info_path,pause

# find the path of the root of the git repostory
# add info in between
git_repo_name = get_repository_name()
# pause(git_repo_name)

program_file_path = os.getcwd()
# pause(program_file_path)

print (get_info_path(program_file_path))