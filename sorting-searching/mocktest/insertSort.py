def insertSort(A):
	"""
	insert Sort demo using python.
	"""

	if isinstance(A, list) != True:
		print "pls enter a list"
		return

	n = len(A)
	if n <= 1:
		return A

	for i in range(1, n):
		for j in range(i-1, -1, -1):
			if A[j] > A[i]:
				A[j], A[i] = A[i], A[j]
				i = i - 1
	return A
