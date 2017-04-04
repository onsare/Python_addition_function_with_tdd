#import unit test
import unittest

def calculateAdditions(expression):
	numbers = expression.split('+')
	total = 0
	for number in numbers:
		total += int(number)
	return total

class TestAdditions(unittest.TestCase):
	def test_one_plus_one(self):
		self.assertEqual(calculateAdditions("1+1"),2)
	def test_negative_one_plus_negative_one(self):
		self.assertEqual(calculateAdditions("-1 + -1"),-2)
	def test_ten_plus_ten(self):
		self.assertEqual(calculateAdditions("10 + 10"),20)
	def test_thousadnd_plus_negative_one(self):
		self.assertEqual(calculateAdditions("1000 + -1"),999)







if __name__ == '__main__':
	unittest.main()

