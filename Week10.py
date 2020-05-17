import os 

filepath = input('Please Enter a Path to be Used: ')
filename = input('Please Enter a File Name to be Used: ' )
filenamefinal = filename + '.txt'

finalpath = filepath + '/' + filenamefinal


if os.path.isdir(filepath): 
	print('Using Existing Directory ')
else:
	os.mkdir(filepath)	
	print('Creating New Directory')

if os.path.isfile(finalpath):	
	print('Editing Existing File')
else:
	print ('Creating New File')
  
if os.path.exists(finalpath): 
	print(finalpath, 'Already Exist')
else:
	print('Path ' + filepath + ' Does Not Exist, File Will Be Created') 

with open(finalpath, 'a') as fileHandle: 
	fileHandle.write ('\n')
	fileHandle.write (input('Please Enter Your Name: '))
	fileHandle.write (', ')			
	fileHandle.write (input('Please Enter Your Address: '))				
	fileHandle.write (', ')	
	fileHandle.write (input('Please Enter Your Phone Number: ')) 
	
with open(finalpath, 'r') as fileHandle: 
	data = fileHandle.read() 
	print(data)
