import os
import time

ret = os.fork()

if ret > 0:
	
	print("11111")
else:
	
	print("00000")

ret = os.fork()

if ret > 0:
	
	print("111")
else:
	
	print("000")
