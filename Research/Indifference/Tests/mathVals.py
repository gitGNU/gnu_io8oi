import random, math, numpy
import unittest




class TestMathFunctions(unittest.TestCase):

    def setUp(self):
	self.returns = [[random.random()*x for x in range(10)] for _ in range(10)]
	self.sds = [[random.random()*x**2 for x in range(10)] for _ in range(10)]
	self.corrMatrix = numpy.corrcoef(self.returns)
	

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)


# Provides commandLine interface
if __name__ == '__main__':
    unittest.main()
