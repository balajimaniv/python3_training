f = open(r'D:\balaji\workspace\python\training\string.txt', "r+")
str = f.read()
print ("reading string: "+str)
# f.readline()



for line in open(r'D:\balaji\workspace\python\training\string.txt') :
	print (line, end = '')

# For input/output : read(),readline, write, writeline()
# tell
position = f.tell()
print ("position:", position)

# seek
position = f.seek(10,0)
print ("position:", position)

# write
f.write("hello world")

str = f.read()
print ("reading string: "+str)

f.close()

import os
print (os.getcwd())
print(os.walk('../../')) 

print (os.cpu_count())

print (os.listdir(os.getcwd()))

