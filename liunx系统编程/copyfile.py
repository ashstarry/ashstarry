import os
from multiprocessing import Pool
from multiprocessing import Manager

def copyFile(name, old, new, q):
	fr=open(old+"/"+name)
	fw=open(new+"/"+name, "w")

	content = fr.read()
	fw.write(content)

	fw.close()
	fr.close()
	#print(name)
	q.put(name)


def main():
	#get the name of file which u want copy
	oldFileName = input("enter the name of file:")

	#create a file
	newFileName = oldFileName + "-copy"
	os.mkdir(newFileName)

	#get all files in the old folder
	fileNames = os.listdir(oldFileName)
	#print(fileNames)
	pool =Pool(5)
	q = Manager().Queue()

	for name in fileNames:
		pool.apply_async(copyFile,args=(name, oldFileName, newFileName,q))

	num = 0
	allNum=len(fileNames)


	while True:
		q.get()
		num += 1
		coppyRate= num / allNum
		print("\r------%.2f%%------"%(coppyRate*100),end="")
		if num == allNum:
			break

	print("finish!!!")
	

if __name__ == '__main__':
	main()