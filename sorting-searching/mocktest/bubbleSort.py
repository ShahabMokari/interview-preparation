def bubbleSort(A):
	"""
	Bubble sorting demo using python.
	"""

	if isinstance(A, list) != True:
		print "pls enter a list"
		return

	n = len(A)
	if n <= 1:
		return A

	for i in range(n-1):
		for j in range(n-1-i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
	return A

