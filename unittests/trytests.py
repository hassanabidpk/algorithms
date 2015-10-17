import unittest 

class TestStringMethods(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		print("hello world")
		
	@classmethod
	def tearDownClass(self):
		print("finish unittest###")	

	@unittest.skip("demonstrating skipping")
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertTrue('FOO'.isupper())
		self.assertGreater(6,4)
		self.assertRegex('abc','[a-z]')
		self.assertDictEqual({'hello':1},{'hello':1})

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])

		with self.assertRaises(TypeError):
			s.split(2)


if __name__ == '__main__':
	print("start unittest ####")
	unittest.main(verbosity=2)

