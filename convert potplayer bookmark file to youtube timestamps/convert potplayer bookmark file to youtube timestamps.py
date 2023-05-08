import sys
import pyperclip

def convert_to_youtube_timestamp(line):
	parts = line.split('*')
	id = parts[0].split('=')[0]

	if (len(parts)>=2):
		# print (parts[0].split('='))

		timestamp = int(parts[0].split('=')[1]) // 1000
		hours = timestamp // 3600
		minutes = timestamp // 60
		seconds = timestamp % 60
		title = parts[1]

		converted_timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d} {title}"
		
		print (converted_timestamp)
		return (converted_timestamp)
	else:
		return ""

def convert_pbf_to_youtube_timestamps(pbf_file):
	with open(pbf_file, 'r', encoding='utf-16') as file:
		lines = file.readlines()[1:]  # Skip the first line
		# Convert each line and then combine them back into a list
		timestamps = [
			convert_to_youtube_timestamp(line)
			for line in lines
				if len(line) > 5  # Skip lines with length <= 5 characters
		]
		# join all items in the list with a newline character
		result = '\n'.join(timestamps)
		pyperclip.copy(result)
		print(result)

if __name__ == '__main__':
	# 0 is the script name
	# 1 is the first argument, i.e. the pbf file
	if len(sys.argv) != 2:
		print("Usage: python script.py <pbf_file>")
	else:
		pbf_file = sys.argv[1]
		convert_pbf_to_youtube_timestamps(pbf_file)
