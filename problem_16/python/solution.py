#!/usr/bin/env python
import sys

def int_to_array(number):
	'''
	Convert integer to list
	'''
	return map(int, str(number))

def double_array_value(arr):
	'''
	double of array_values
	'''
	max_length = len(arr)
	
	# total = [None] * max_length
	remainder = 0
	for i in xrange(max_length):
		# total[i] = (get_element(arr, i) + get_element(arr, i) + remainder) % 10
		total = (arr[i]*2)+remainder
		arr[i] = total % 10
		remainder = total / 10

	if remainder > 0:
		arr.append(remainder)
	return arr

def two_pow_any(exponent):
	# The shop is closed! See you soon!
	# print exponent
	if exponent >= pow(10, 9) or exponent < 0:
		print 'Crazy!!'
		return -1

	# OK, but too easy!
	if 1 < exponent <= 100:
		return sum(int_to_array(pow(2, exponent)))

	# Main deal here
	one = int_to_array(pow(2, 100))[::-1]
	i = 101
	while i <= exponent:
		one = double_array_value(one)
		i += 1

	return sum(one)
	
assert 7 == two_pow_any(10)
assert 26 == two_pow_any(15)
print two_pow_any(int(sys.argv[1]))

'''
$ time ./solution.py 100000
135178

real	5m11.188s
user	5m10.832s
sys	0m0.068s
'''