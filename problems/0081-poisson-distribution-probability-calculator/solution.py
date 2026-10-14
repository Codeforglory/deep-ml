import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	# Your code here
	import numpy as np
	k_fact = 1
	for i in range(2,k + 1,1):
		k_fact *= i
	val = ((math.exp(-lam))*(lam ** k))/k_fact

	return round(val,5)