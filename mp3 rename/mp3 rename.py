import os
import eyed3

root_path="E:/Data/Cache/Downloads/"
# root_path="E:/Data/Cache/Downloads/The Queen of Crows/"
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
        # print("wtf",tmp)

        if (os.path.exists(root_path+tmp)==0):
            print(tmp)
            os.rename(root_path+os.path.join(file),root_path+tmp)
        elif (os.path.join(file)!=tmp):
            print(file+" file name conflicts")