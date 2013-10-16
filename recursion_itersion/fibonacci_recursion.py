def fibonacci(n):
	# n is non negitive integer
	if n < 0:
		print 'n should be non negitive'
		return
	elif n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

