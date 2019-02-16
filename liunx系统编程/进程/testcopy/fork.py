import os
import time

ret = os.fork()

if ret > 0:
	
	print("11111")
else:
	time.sleep(3)
	print("00000")
