import os
 
class readFile:
	def readfile(self,filename):
		if os.path.isfile(filename) : 
			f = open(filename)
			lines=f.readlines()
			while lines:
				return lines
				lines = f.readlines()  
			f.close()
		else :
			print('File does not exists.')
			
	def  dispose(self):  
		pass  


