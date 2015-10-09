
from unittest import TestCase, main

class Tests(TestCase):
	def test_one(self):
		names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
		r = 1
		res = "Sheldon"
		self.assertEquals(whoIsNext(names, r), res)


if __name__ == "__main__": main()