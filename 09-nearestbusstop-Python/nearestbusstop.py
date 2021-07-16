# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.

import math

def fun_nearestbusstop(street):
	num = street % 8
	if (num <= 4):
		res = (street//8)*8
		return res 
	elif (num > 4):
		res = ((street//8)+1)*8
		return res
