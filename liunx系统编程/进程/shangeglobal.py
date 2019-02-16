import os
import time

g=100

ret = os.fork()

if ret == 0:
	g += 1
	print("%d"%g)
else:
 	time.sleep(1)
 	print("%d"%g)