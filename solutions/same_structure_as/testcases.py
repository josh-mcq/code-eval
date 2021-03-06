from unittest import TestCase, main

class Test(TestCase):

    def test_file(self):

		
		self.assertEquals(same_structure_as([1,1,1],[2,2,2]), True, "[1,1,1] same as [2,2,2]")
		self.assertEquals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
		self.assertEquals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
		self.assertEquals(same_structure_as([1,[1,1]],[2,[2]]), False, "[1,[1,1]] not same as [2,[2]]")

		
		self.assertEquals(same_structure_as([[[],[]]],[[[],[]]]), True, "[[[],[]]] same as [[[],[]]]")
		self.assertEquals(same_structure_as([[[],[]]],[[1,1]]), False, "[[[],[]]] not same as [[1,1]]")
	def test_file2(self):

		
		self.assertEquals(same_structure_as([1,[[[1]]]],[2,[[[2]]]]), True, "[1,[[[1]]]] same as [2,[[[2]]]]")

		
		self.assertEquals(same_structure_as([],1), False, "[] not same as 1")
		self.assertEquals(same_structure_as([],{}), False, "[] not same as {}")

		
		self.assertEquals(same_structure_as([1,'[',']'],['[',']',1]), True, "[1,'[',']'] same as ['[',']',1]")