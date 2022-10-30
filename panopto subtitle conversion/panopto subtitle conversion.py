import sys
import os

# argv[0] is the script itself.
# get the arguments from 1 to the end
file_list = sys.argv[1:]
# print (file_list)

for file in file_list:
	# print (file)
	with open(file,'r',encoding='utf-8') as f:
		# print (f.readlines())
		cnt = 0
		s = ""
		# os.system("pause")
		for line in f.readlines():
			line = line.strip()

			colon_pos=line.find(":")
			if (colon_pos=="-1" or len(line)>=8):
				# it does not have colon or it's longe enough -> it's a timestamp
				s += line+" "

	with open(file,'w',encoding='utf-8') as f:
		cnt = 0
		# with an space, more likely to be the end of a sentence
		paragraph = s.split(".")

		# print(paragraph)

		for i,sentence in enumerate(paragraph):
			# output the chars at the end of previous sentence first
			if (i>0): f.write('.')
			pos=0
			for c in sentence:
				if (c.isalnum() or c==' '): break
				f.write(c)
				pos+=1

			sentence = sentence[pos:]


			if (i>0):
				if (sentence[0].isalnum()==0 and ('a'<=sentence[1]<='z')==0):
					# short/long sentence
					f.write("\n\n")

				elif (sentence[0].isalnum()==0):
					# long non-sentence: G.P.A [of xxxxx]
					f.write(" ")

				else:
					# short non-sentence: U.[S.]
					f.write("")

			sentence = sentence.strip()

			if (sentence==""): continue

			f.write(sentence)

# special case
# short non-sentence: the U.S. accounted for 14.5%
# of the Qing dynasty emperor.Cha Ching was the son and successor of Emperor (乾隆,1735 to 1796) under whom China achieved the zenith of its power and wealth.
# She said "wtf." IDK.