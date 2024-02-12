import os
from print_divider import print_divider

os.system("winget upgrade")

print_divider()
upgrade_input = input("Do you want to upgrade all packages? ( [y] / n / <package names separated by a single space>): ")
print_divider()

if upgrade_input == "y" or upgrade_input == "Y" or upgrade_input == "":
    os.system("winget upgrade --all --silent --accept-package-agreements --accept-source-agreements")
elif upgrade_input == "n" or upgrade_input == "N":
    pass
else:
    os.system(f"winget upgrade {upgrade_input} --silent --accept-package-agreements --accept-source-agreements")

print_divider()
os.system("pause")