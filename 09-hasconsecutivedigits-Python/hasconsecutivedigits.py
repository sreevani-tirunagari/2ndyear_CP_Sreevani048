# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	x = [int(i) for i in str(abs(n))]
	a = []
	for i in x:
		count = x.count(i)
		if (count>1):
			a.append(i)
	if (len(a)==0):
		return False
	else:
		return True