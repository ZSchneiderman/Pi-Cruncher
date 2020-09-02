
# Zachary Schneiderman 
# Machin's Arctan Pi Computation
# Ver 1.0 -- 9/2/2020
# ----------------------------------------------
# Arctan function error optimized for precision
# x : Machin's Coefficients
# digits : Desired number of digits of pi to compute
# returns the arctan of Machin's Coefficients

def arctan(x, digits):

	short_div = 10**digits    
	p = short_div // x		# Use short division for M*N operations --> 1/x^n
	total = p			# Summation accumulator for arctan function
	d = 1				# Compute the odd nth term of the summation
	
	while True:
		p = -p // x**2
		d += 2			# Compute odd terms of the summation
		delta = p // d		
		if delta == 0:
			break		# Break when summation converges
		total += delta		# Accumulate summation until convergeance
	return total


digits = 100000 			# Number of digits to compute
print 4*(4*arctan(5, digits) - arctan(239, digits))
		
		
		
		
		
		
		
		
		
		
		
