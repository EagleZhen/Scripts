from PIL import Image
import infi.systray
from os.path import dirname,join,abspath
from ez import pause

from win11toast import ToastNotifier

def show_notification():
    toaster = ToastNotifier()
    toaster.show_toast("Notification Title", "Notification Message", duration=5)

menu_options = (("Show Notification", None, show_notification),)

def hello(systray):
	print("Hello!")

# Load the tray icon image using relative path to the script directory
script_dir = dirname(abspath(__file__))
icon_path = join(script_dir, "../icon.ico")

# Create the tray icon menu
# "Hello": text label for the option
# None: icon for the option
# hello: callback function for the option
menu_options = (("Hello", None, hello),)

pause (icon_path)

# # Create the tray icon object
systray_options = {
	"menu_options": menu_options,
	"icon": icon_path,
	"hover_text": "auto connect cuhk wired network",
}
tray = infi.systray.SysTrayIcon(**systray_options)

# Start the tray icon event loop
tray.start()