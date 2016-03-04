def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)
from unittest import TestCase, main

class Test(TestCase):

    def test_file(self):

		
		self.assertEquals(same_structure_as([1,1,1],[2,2,2]), True, "[1,1,1] same as [2,2,2]");
		self.assertEquals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
		self.assertEquals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
		self.assertEquals(same_structure_as([1,[1,1]],[2,[2]]), False, "[1,[1,1]] not same as [2,[2]]")

		
		self.assertEquals(same_structure_as([[[],[]]],[[[],[]]]), True, "[[[],[]]] same as [[[],[]]]")
		self.assertEquals(same_structure_as([[[],[]]],[[1,1]]), False, "[[[],[]]] not same as [[1,1]]")

		
		self.assertEquals(same_structure_as([1,[[[1]]]],[2,[[[2]]]]), True, "[1,[[[1]]]] same as [2,[[[2]]]]")

		
		self.assertEquals(same_structure_as([],1), False, "[] not same as 1")
		self.assertEquals(same_structure_as([],{}), False, "[] not same as {}")

		
		self.assertEquals(same_structure_as([1,'[',']'],['[',']',1]), True, "[1,'[',']'] same as ['[',']',1]")