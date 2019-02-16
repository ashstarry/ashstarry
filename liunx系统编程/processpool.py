from multiprocessing import Pool
import random
import time
import os


def worker(num):
	for i in range(5):
		print("pid==%d==%d"%(os.getpid(), num))
		time.sleep(1)



pool=Pool(3)

for i in range(10):
	print("-------%d-------"%i)
	pool.apply_async(worker,(i,))


pool.close()
pool.join()