# set environment path to add this module into the serach path list of python
import time
import sys
import keyboard
import os
import shutil
import subprocess
import win11toast


# 按住大写键停止程序
def check_force_stop():
    if keyboard.is_pressed("capslock"):
        sys.exit("\aSir, I have stopped the program for you.")


def notify(title, message):
    win11toast.notify(title=title, body=message)


def print_divider(size=50):
    """
    Print ================================================== by default. 
    
    The size can be changed.
    """
    print(f"\n{'='*size}\n")


# 移动文件，前面是file，后面是folder
def move_file(source, destination):
    if os.path.exists(source):
        os.makedirs(destination, exist_ok=True)
        shutil.move(source, destination)
        print("================\n", source, "\nhas been moved to\n", destination, "\n================")
    else:
        print(source + " not exist")


# 复制文件，前面是file，后面是folder
# 如果同名会覆盖
def copy_file(source, destination):
    if os.path.exists(source):
        os.makedirs(destination, exist_ok=True)
        shutil.copy(source, destination)
        print("================\n", source, "\nhas been copied to\n", destination, "\n================")
    else:
        print(source + " not exist")


def rename_file(old_name, new_name, manual=False):
    try:
        os.rename(old_name, new_name)
        if manual:  # if the function is called by user, print a message
            print(f"File renamed from '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{old_name}' not found.")
    except FileExistsError:
        if manual:
            choice = input(
                f"A file with the name '{new_name}' already exists.\nDo you want to overwrite it? (yes/no): "
            )
            if choice.lower() == "yes":
                os.remove(new_name)  # Remove the existing file
                os.rename(old_name, new_name)
                print(f"File renamed from '{old_name}' to '{new_name}'.")
            else:
                choice = input("Do you want to enter a new name for the file? (yes/no): ")
                if choice.lower() == "yes":
                    new_name = input("Enter a new name for the file: ")
                    rename_file(old_name, new_name, manual)  # Recursively call the function with the new name
                else:
                    # Should not continue, as it may cause program like "categorize videos.py" to handle the file name incorrectly
                    sys.exit("Operation aborted by user.")
        else:
            sys.exit(f"Error: A file with the name '{new_name}' already exists.")


def print_message(*args):
    message = " ".join(str(arg) for arg in args)
    print(message)


def pause(*args):
    print_message(*args)
    os.system("pause")


def stop(*args):
    print_message(*args)
    sys.exit()


def get_repository_name():
    try:
        # get the repository url from local git config file
        output = subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
        # convert bytes to string and split by '/'
        url_parts = output.decode().strip().split("/")
        repository_name = url_parts[-1].replace(".git", "")
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
def get_info_path():
    program_file_path = os.getcwd()
    git_repo_name = get_repository_name()
    info_folder = "info for program"
    # get the root path of the git repository
    root, script_folder = program_file_path.split(f"\\{git_repo_name}")
    script_folder = script_folder[1:]  # remove the '\' at the beginning
    if script_folder == "":  # when the script is in the root folder of the git repository
        script_folder = git_repo_name

    # pause("root: "+root)
    # pause("script: "+script_folder)

    info_path = f"{root}\\{git_repo_name}\\{info_folder}\\{script_folder}"

    return info_path


if __name__ == "__main__":
    print(get_info_path(os.path.abspath(__file__)))
