import re

def convert_stream_info(input_text, output_file):
    # Split the input text into lines and remove empty lines
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]
    
    # Initialize the output content
    output = []
    
    # Process the general section
    output.append(f"{lines[1]}\t")
    output.append(f"{lines[3]} Choose 17 units from\t")
    output.append("Course Code\tElite Stream")
    
    # Extract and format course information
    courses = re.split(r',\s*', lines[5].replace("and", ","))
    
    for course in courses:
        if '/' in course:
            code, elite = course.split('/')
            output.append(f"{code.strip()}\t{elite.strip()}")
        else:
            output.append(f"{course.strip()}\t")
    
    # Process the specific stream section
    output.append(f"\n{lines[6]}\t")
    output.append(f"{lines[8]}\t")
    output.append(f"{lines[9]}\t")
    
    # Extract and format required course information
    req_courses = re.split(r',\s*', lines[11].replace("and", ","))
    for course in req_courses:
        if '/' in course:
            code, elite = course.split('/')
            output.append(f"{code.strip()}\t{elite.strip()}")
        else:
            output.append(f"{course.strip()}\t")
    
    # Process the elective courses section
    output.append(f"{lines[13]}\t")
    output.append(f"{lines[14]} Choose at least 9 units from the following:\t")
    
    # Extract and format elective course information
    elective_courses = re.split(r',\s*', lines[16].replace("and", ","))
    for course in elective_courses:
        if '/' in course:
            code, elite = course.split('/')
            output.append(f"{code.strip()}\t{elite.strip()}")
        else:
            output.append(f"{course.strip()}\t")
    
    # Process the remaining units section
    output.append(f"{lines[18]}\t")
    output.append(f"{lines[19]}\t")
    
    # Extract and format remaining units course information
    remaining_courses = re.split(r',\s*', lines[21].replace("and", ","))
    for course in remaining_courses:
        if '/' in course:
            code, elite = course.split('/')
            output.append(f"{code.strip()}\t{elite.strip()}")
        else:
            output.append(f"{course.strip()}\t")
    
    # Write the output to the output file
    with open(output_file, 'w') as file:
        file.write("\n".join(output))

# Input text
input_text = """
(a)

General Computer Science

 

 

Elective Courses:

 

 

Choose 17 units from AIST4010/ESTR4140, CSCI3220/ESTR3110, CSCI3230/ESTR3108, CSCI4180/ESTR4106, CSCI4250/ESTR4122, CSCI4430/ESTR4120, ENGG1820, (ENGG3802 and 3803), IERG4300/ESTR4300, STAT2005, 2006 and the AIST/CENG/CSCI courses of which at least 15 units must be from courses at 3000 or above level
(b)

Stream 1: Intelligence Science

 

 

Required Courses:

 

 

CSCI3230/ESTR3108

 

 

Elective Courses:

 

 

Choose at least 9 units from the following:

 

 

AIST3510/SEEM3510, AIST4010/ESTR4140, CSCI3220/ESTR3110, CSCI3320, 4190, 4230, CSCI4250/ESTR4122, CSCI5030, 5050, 5150, CSCI5160/ENGG5102, CSCI5170, CSCI5180/ENGG5103, CSCI5240, CSCI5250/ENGG5106, CSCI5280/ENGG5104, CSCI5350, 5390, CSCI5510/ENGG5108, CSCI5580, 5640, ENGG5781, IERG3320, IERG4300/ESTR4300

 

 

Remaining units can be chosen from the following:

 

 

AIST/CENG/CSCI courses at 2000 or above level, ENGG1820, (ENGG3802 and 3803), STAT2005, 2006
"""

# Output file path
output_file = 'output_stream_info.txt'

# Convert the input text
convert_stream_info(input_text, output_file)

print(f"Converted text has been written to {output_file}")
