""" 
Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. 
More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. 
All numbers at input are integers of one or two digits.
"""

import sys

def find_answer():
	number = int(sys.stdin.readline())
	while(number != 42):
		print(number)
		number = int(sys.stdin.readline())

if __name__ == '__main__':
	find_answer()