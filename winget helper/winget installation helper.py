import os
from ez import print_divider

package_keyword = input("Package to be searched: ")

print_divider()

os.system(f"winget search \"{package_keyword}\"")

print_divider()

package_name = input("Package to be installed: ")
silent_install = input("Silent install? ( [y] /n ): ")

print_divider()

command = f"winget install {package_name}"
additional_arguments_for_silent_install = " --silent --accept-package-agreements --accept-source-agreements"

if silent_install == "y" or silent_install == "":
    command += additional_arguments_for_silent_install

os.system(command)

print_divider()

os.system("pause")