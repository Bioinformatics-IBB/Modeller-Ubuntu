import os
import glob

list1 = os.listdir(os.getcwd())

for x in list1:
	nameOfFile = (x[:5]+x[-5:])
	os.rename(x, nameOfFile)
