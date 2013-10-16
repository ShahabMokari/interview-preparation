def fibonacci(n):
	if n < 0:
		print "n should be non negitive"
		return

	f = [None]*2
	f[0], f[1] = 0, 1
	for i in range(2, n+1):
		f[1], f[0] = f[0] + f[1], f[1]
	return f[1]
