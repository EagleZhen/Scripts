import os
import eyed3

f = open('path.txt','r',encoding='utf-8')
root_path = f.readline()
print (root_path)
os.system("pause")

root_path=root_path.replace("\\","/")+"\\"
file_list=os.listdir(root_path)

# eyed3.log.setLevel("ERROR")

for file in file_list:
    # print (os.path.splitext(file))
    if (os.path.splitext(file)[1]==".mp3"):
        audio_file=eyed3.load(root_path+os.path.join(file))
        
        artist=audio_file.tag.artist
        artist=artist.replace("/",",")

        title=audio_file.tag.title
        title=title.replace("/"," ")

        tmp=artist+" - "+title+".mp3"

        # check name conflicts
        if (os.path.exists(root_path+tmp)==0):
            print(tmp)
            os.rename(root_path+os.path.join(file),root_path+tmp)
        else:
            print("[ "+file+" ] file name conflicts")