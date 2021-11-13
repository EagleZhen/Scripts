import os
import json
import ez
import sys

# 将stdout转做同文件夹下的file output，方便查看
sys.stdout = open(os.path.dirname(__file__)+"/output.txt","w")

original_path = "D:/Games/Minecraft/Minecraft - HMCL/1.12.2/resourcepacks/【1.12 IT-Project】PCMS/"
overlay_path = "D:/Games/Minecraft/Minecraft - HMCL/1.12.2/resourcepacks/PCMS - Overlay with IT-Project/"
loop_path = overlay_path+"assets/minecraft/models/"
copy_path = original_path+"assets/minecraft/textures/"
paste_path = overlay_path+"assets/minecraft/textures/"

# 存储是否有已经移动过该文件
exist={}

for root, subdirectories, files in os.walk(loop_path):
    # 遍历所有文件里的文件，包括子文件夹里面的

    for file in files:
        # 只查看json文件
        if (file.find(".json") != -1):
            full_file_name = root+"/"+file
            file_object = open(full_file_name)
            # print("**",full_file_name)

            # 将json文件转成dictionary
            data = json.load(file_object)

            for i in data["textures"]:
                # 未移动过
                if ((data["textures"][i] in exist) == False):
                    exist[data["textures"][i]] = True

                    # print(data["textures"][i])
                    src = copy_path+data["textures"][i]+".png"

                    # 找到string里面最后出现的"/"，只要前面的文件夹路径
                    pos = data["textures"][i].rfind("/")
                    dest = paste_path+data["textures"][i][0:pos]

                    # print (pos,data["textures"][i][0:pos])

                    # print(src)
                    # print(dest)
                    
                    if (os.path.exists(src)):
                        print (data["textures"][i]+".png")

                    # 还没移动才移动
                    if (os.path.exists(src)==False):
                        ez.copy_file(src,dest)
                    # quit()


            file_object.close()

# D:/Games/Minecraft/Minecraft - HMCL/1.12.2/resourcepacks/【1.12 IT-Project】PCMS/assets/minecraft/models/blocks/bedrock.png
# D:\Games\Minecraft\Minecraft - HMCL\1.12.2\resourcepacks\【1.12 IT-Project】PCMS\assets\minecraft\textures\blocks\bedrock.png