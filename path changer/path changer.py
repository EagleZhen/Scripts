import pyperclip

s=input().replace("\\","/")
s=s.replace("\"","")
s=s.replace("filelist:","")

pyperclip.copy(s)
print(pyperclip.paste())
