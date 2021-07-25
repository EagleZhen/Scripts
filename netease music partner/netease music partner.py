import ez

#start evaluating
ez.mouse.move(731,737)
ez.mouse.click()
ez.time.sleep(5)

#start playing songs
ez.mouse.move(561,714)
ez.mouse.click()
ez.time.sleep(1)

for i in range(5):
	print (i+1,end=" ")

	#scroll
	ez.mouse.wheel(-3)
	ez.time.sleep(20);

	#three stars
	ez.mouse.move(737,754)
	ez.mouse.click()
	ez.time.sleep(1)

	#唱功不错+音色独特+情感到位
	ez.mouse.move(632,652)
	ez.mouse.click()
	ez.time.sleep(1);

	ez.mouse.move(734,652)
	ez.mouse.click()
	ez.time.sleep(1)

	ez.mouse.move(839,652)
	ez.mouse.click()
	ez.time.sleep(1);

	#提交
	ez.mouse.wheel(-3)
	ez.time.sleep(1);

	ez.mouse.move(752,734)
	ez.mouse.click()
	ez.time.sleep(5)

	print ("done")