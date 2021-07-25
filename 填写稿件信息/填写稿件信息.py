import ez

f = open("info.txt", "r",encoding="utf-8")
song_name=f.readline()
song_name=song_name.replace("EagleZhen - ","")

text=""

lines=f.readlines()
for line in lines:
	text+=line

ez.mouse.move(619,410)
ez.mouse.click()

ez.mouse.move(1002,458)
ez.mouse.click()

ez.mouse.move(713,509)
ez.mouse.click()

ez.mouse.move(402,451)
ez.mouse.click()
ez.time.sleep(0.5)

for i in range(7):
	ez.keyboard.send("tab")

ez.keyboard.write(song_name)
ez.keyboard.send("tab")

ez.keyboard.write("EagleZhen")
ez.keyboard.send("tab")

# ez.keyboard.write("钢琴")
ez.keyboard.send("tab")

ez.keyboard.write("EagleZhen")
ez.keyboard.send("tab")

ez.keyboard.write("EagleZhen")
ez.keyboard.send("tab")

ez.keyboard.write("EagleZhen")
ez.keyboard.send("tab")

ez.keyboard.write("来自网络，感谢原作者")
ez.keyboard.send("tab")

ez.keyboard.send("tab")
ez.keyboard.send("tab")
ez.keyboard.write(text)