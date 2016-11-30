from readfile import readFile
import unittest

class rfTestCase(unittest.TestCase):
	
	def setUp(self):
		self.rf = readFile()
		
	def tearDown(self):
		self.rf.dispose()
		self.rf = None
		
	def testfileIsExit(self):
		fn = "test.py"	
		result = self.rf.readfile(fn)
		self.assertEqual(str(result),"None")
		print ("This file is empty!")
		
	def testfileContent(self):
		filename = "apiTest.txt"
		text = self.rf.readfile(filename)
		ll = len(text)
		self.assertEqual(str(ll),"2")
		print("This file has two rows!")

if __name__ == "__main__":
	#unittest.main()
	runner = unittest.TextTestRunner()
	suite = unittest.TestSuite()
	suite.addTest(rfTestCase("testfileIsExit"))
	suite.addTest(rfTestCase("testfileContent"))
	runner.run(suite)