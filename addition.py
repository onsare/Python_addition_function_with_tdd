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

def calculateSubtractions(expression):
	numbers = expression.split('-')
	total = 0
	for number in numbers:
		total -= int(number)
	return total

class TestAdditions(unittest.TestCase):
	def test_one_minus_one(self):
		self.assertEqual(calculateSubtractions("1-1"),0)
	def test_negative_one_minus_negative_one(self):
		self.assertEqual(calculateSubtractions("-1 - 1"),-2)
	







if __name__ == '__main__':
	unittest.main()

# formula for getting interest rate A = P(1 + rt)
# r is the decimal form of R/100; r and t are in the same units of time
