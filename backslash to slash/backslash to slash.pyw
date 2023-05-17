import pyperclip
from win11toast import toast

content = pyperclip.paste()
pyperclip.copy(content.replace("\\","/"))

toast_content = "=====original====\n" + content + "\n=====replaced====\n" + pyperclip.paste()

toast(toast_content)