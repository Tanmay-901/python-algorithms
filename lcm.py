from math import *

#Calculates Lowest Common Multiple
def compute_lcm(x, y):

	# Select larger number
	if x > y:
	  	larger = x
	else:
		larger = y

	# Checks if the larger value is divisible by both numbers
	while((larger % x != 0) or (larger % y != 0)):
			# If not divisible by either number, the larger value is incremented by 1
	    larger += 1

	return larger

in1 = int(input("Insert 1st number: "))
in2 = int(input("Insert 2nd number: "))

print("LCM of %d and %d is"%(in1, in2), compute_lcm(in1, in2))