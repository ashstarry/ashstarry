from multiprocessing import Process
import time
import random

class myProcess(Process):
	def run(self):
		while 1:
			print("111111")
			time.sleep(1)


p = myProcess()
p.start()

while 1:
	print("main")
	time.sleep(1) 
	