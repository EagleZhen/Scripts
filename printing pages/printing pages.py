import pyperclip
import time

multiple=int(input("Number of pages in a A4 page? (1/2) = "))
number_of_page=int(input("Total number of pages in one A4 page = "))

if (number_of_page==1):
	if (number_of_page%2==1):
		print(number_of_page)
		number_of_page-=1

	for i in range(2,number_of_page+1,2):
		print(i,",",end="")
	print("")

	for i in range(number_of_page,0,-1):
		print(i,",",end="")
	print("")

else:
	if (number_of_page%2==1):
		print(number_of_page)
		number_of_page-=1

	for i in range(3,number_of_page+1,4):
		print(i,",",end="")
	print("")

	for i in range(number_of_page,0,-1):
		print(i,",",end="")
	print("")