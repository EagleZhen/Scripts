import pyperclip

s=pyperclip.paste()+"\\"
pyperclip.copy(s.replace("\\","/"))
print(pyperclip.paste())

# D:\Github\Scripts\path changer