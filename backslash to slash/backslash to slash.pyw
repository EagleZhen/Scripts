import pyperclip
from ez import notify

content = pyperclip.paste()
result = content.replace('\\', '/')
pyperclip.copy(result)
notify(title="Copied to the clipboard", message=f"\n{result}")