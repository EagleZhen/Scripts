import sys
import os
import re

# argv[0] is the script itself.
# get the arguments from 1 to the end
file_list = sys.argv[1:]
# print (file_list)

for file in file_list:
	# print (file)
	with open(file,'r',encoding='utf-8') as f:
		# print (f.readlines())
		cnt = 0
		text = ""
		# os.system("pause")
		for line in f.readlines():
			line = line.strip()

			colon_pos=line.find(":")
			if (colon_pos=="-1" or len(line)>=8):
				# it does not have colon or it's longe enough -> it's a timestamp
				text += line+" "

	# extract one sentence from the string each time
	paragraph = []
	s=""
	for c in text:
		s+=c
		if (c=='?' or c=='.' or c=='!'):
			paragraph.append(s)
			s=""
	paragraph.append(s)

	with open(file,'w',encoding='utf-8') as f:
		len_previous_sentence = 0

		for i,sentence in enumerate(paragraph):
			# print("==========",sentence)

			print (i, paragraph[i], len(paragraph[i]), len_previous_sentence)

			# decide the connection between two elements in the list
			if (i>0):
				# current element is long enough
				# first char of current element not letter or number (space or endline), 
				# second letter of current element is letter
				# and the previous element is long enough
				# then it's very likely to be the start of a new sentence

				if (len(sentence)>=2 and sentence[0].isalnum()==0 and sentence[1].isalnum()):
					if (len_previous_sentence>20):
						f.write("\n\n")
					else:
						f.write(" ")
					len_previous_sentence=len(sentence)

				# first char of current element not letter or number (space or endline), 
				# last element may not be long enough
				# so possibly the middle of a sentence, not the start
				# G.P.A.[ of xxxxx] , Dr.[ James]
				elif (sentence[0].isalnum()==0):
					f.write(" ")
					len_previous_sentence+=len(sentence)

				# short non-sentence
				# U.[S.]
				else:
					f.write("")
					len_previous_sentence+=len(sentence)

			sentence = sentence.strip()

			if (sentence==""): continue

			f.write(sentence)

# special case
# short non-sentence: the U.S. accounted for 14.5%
# of the Qing dynasty emperor.Cha Ching was the son and successor of Emperor (乾隆,1735 to 1796) under whom China achieved the zenith of its power and wealth.
# She said "wtf." IDK.
# Dr. James like you. Your G.P.A. is high. WTF is Dr. James. 