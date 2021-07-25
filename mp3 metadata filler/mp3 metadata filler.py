import os
import eyed3

root_path="E:/Data/Cache/Downloads/"
file_list=os.listdir(root_path)

eyed3.log.setLevel("ERROR")

for file in file_list:
    # print (os.path.splitext(file))
    if (os.path.splitext(file)[1]==".mp3"):
        file_name=os.path.splitext(file)[0]
        # print (file_name)
        artist,title = file_name.split(" - ")
        print ("Artist: ",artist," - ","Title: ",title,sep="")
        # print (os.path.join(file))
        audio_file=eyed3.load(root_path+os.path.join(file))
        audio_file.tag.artist=artist
        audio_file.tag.album=title
        audio_file.tag.title=title
        # if (audio_file.comments!=""):
        #     del audio_file.tag.frame_set[eyed3.id3.frames.COMMENT_FID]
        audio_file.tag.save()